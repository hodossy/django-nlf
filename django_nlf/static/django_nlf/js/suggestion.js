(function (root, factory) {
  'use strict';

  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define('DjangoNLF', [], factory);
  } else if (typeof exports === 'object') {
    // Node. Does not work with strict CommonJS, but
    // only CommonJS-like environments that support module.exports,
    // like Node.
    module.exports = factory();  // eslint-disable-line
  } else {
    // Browser globals (root is window)
    root.DjangoNLF = factory();  // eslint-disable-line
  }
}(this, function () {
    'use strict';

    function logError(msg, context) {
      console.error('DjangoNLF: ' + msg, context);
    }

    function breakBy(value, separator = /\s+/) {
      const match = value.match(separator);
      if (match === null) {
        return [ value, "" ];
      }
      return [
        value.substr(0, match.index),
        value.substr(match.index + match[0].length)
      ]
    }

    function trimStart(value, chars) {
      for (let char of chars) {
        if (value.indexOf(char) === 0) {
          value = value.slice(1);
        }
      }
      return value;
    }

    function Suggestion(value, display, help) {
      this.value = value;
      this.display = display;
      this.help = help || '';
    }

    function generateGetObjects(objectsPropName) {
      objectsPropName = objectsPropName || 'results';
      return function drfResults(response) {
        // paginated list views have a 'results' property,
        // otherwise the response itself is the list
        return response[objectsPropName] || response;
      }
    }

    function defaultOptionDisplay(obj, field) {
      return obj
    }

    var Suggester = function(options) {
      if (options['schema'] === undefined && options['schemaUrl'] === undefined ) {
        throw Error("Either 'schema' or 'schemaUrl' option must be defined!");
      }
      this.schema = options['schema']
      if (this.schema === undefined) {
        this.fetchSchema(options['schemaUrl']);
        this.baseModel = options['schemaUrl'].split("/").slice(-2).join(".");
      } else {
        this.baseModel = options['baseModel'] || Object.getOwnPropertyNames(this.schema)[0];
      }

      this.getObjects = options['getObjectsFn'] || generateGetObjects(options['objectsProperty']);
      this.optionDisplay = options['optionDisplayFn'] || null;
      this.optionHelp = options['optionHelpFn'] || null;
      this.logger = options['logger'] || {error: logError};

      this.loading = false;
      this.onloadingchange = null;
      this.ongoingRequest = null;
    }

    Suggester.prototype = {
      booleanSuggestions: [
        new Suggestion('true ', 'True', ''),
        new Suggestion('false ', 'False', ''),
      ],
      notSuggestion: new Suggestion('not ', 'not', ''),
      operatorSuggestions: [
        new Suggestion('and ', 'and', ''),
        new Suggestion('or ', 'or', ''),
        new Suggestion('and not ', 'and not', ''),
        new Suggestion('or not ', 'or not', ''),
      ],
      lookupSuggestions: [
        new Suggestion('is ', 'is', 'equals or "="'),
        new Suggestion('is not ', 'is not', 'does not equal or "!="'),
        new Suggestion('contains ', 'contains', ''),
        new Suggestion('does not contain ', 'does not contain', ''),
        new Suggestion('matches ', 'matches', '~'),
        new Suggestion('does not match ', 'does not match', '!~'),
        new Suggestion('in (', 'in', ''),
        new Suggestion('not in (', 'not in', ''),
        new Suggestion('> ', 'greater than', '>'),
        new Suggestion('>= ', 'greater than or equal', '>='),
        new Suggestion('< ', 'lower than', '<'),
        new Suggestion('<= ', 'lower than or equal', '<='),
      ],
      alternativeLookups: [">", ">=", "<", "<=", "equals", "does not equal"],
      fnRegex: /\w+\(/,

      isBooleanShortcut: function(field) {
        if (!field.startsWith("is")) {
          return false;
        }
        const fieldPath = field.split(' ').slice(-1)[0];
        const fieldSchema = this.schema[this.baseModel]['fields'][fieldPath]
        return fieldSchema && fieldSchema["type"] === "boolean";
      },

      isFunction: function(value) {
        const match = value.match(this.fnRegex);
        return match && match.length > 0;
      },

      scopeAfterFunction: function(value, field) {
        const model = field ? this.getModelFromPath(field) : this.baseModel;
        const openParenIndex = value.indexOf("(");
        if ( openParenIndex > 0 && value.indexOf(")") === -1) return 'function';

        const fnName = value.substr(0, openParenIndex);
        const fn = this.schema[model]['functions'][fnName] || this.schema["common_functions"][fnName];

        if (fn['role'] === "field") return "lookup";
        // value and expression functions
        return "operator";
      },

      checkLookup: function (value) {
        // check for 'do(es) ...' and 'not in'
        if (value.startsWith('d') || value.startsWith('n')) return 'partial';

        const isFull = this.lookupSuggestions.some((lookup) => {
          return lookup.display === value;
        });
        if (isFull) return 'full';

        return 'partial';
      },

      getContext: function(expression) {
        var context = {
          scope: null,
          model: this.baseModel,
          field: null,
          searchTerm: "",
        };
        var lookBehindTokens = [];

        var rest = expression.replace(/\s+/, " ");
        var currentToken = null;
        var endsWithSpace = rest.endsWith(" ");
        var extendSearchTerm = false;
        do {
          [currentToken, rest] = breakBy(rest);
          if (!rest && endsWithSpace) {
            rest = " ";
            endsWithSpace = false;
          }

          switch (context.scope) { // prepresents previous scope
            case null:
              // handle when negated  or grouped instantly
              if (currentToken === 'not' || currentToken === '(' && !!rest) {
                break;
              }
              // first token must be a field
              if (currentToken.length || !rest) {
                // if it starts with a parenthesis, it is a grouping,
                // therefore a field follows
                context.scope = this.isFunction(currentToken)
                  ? 'function'
                  : 'field';
              }
              break;
            case 'field':
              if (context.searchTerm === 'is' || context.searchTerm === 'is not') {
                extendSearchTerm = true;
              } else {
                context.field = context.searchTerm.startsWith('(')
                ? context.searchTerm.slice(1)
                : context.searchTerm.split(' ').slice(-1)[0];
                context.scope = this.isBooleanShortcut(context.searchTerm) ? 'operator' : 'lookup';
              }
              break;
            case 'lookup':
              switch (this.checkLookup(context.searchTerm)) {
                case 'full':
                  if (context.searchTerm === 'is' && currentToken === 'not') {
                    extendSearchTerm = true;
                  } else {
                    context.scope = this.isFunction(currentToken)
                    ? "function"
                    : currentToken.startsWith('(')
                      ? 'list-value'
                      : currentToken.startsWith('"')
                        ? 'quoted-value'
                        : 'value';
                  }
                  break;
                case 'partial':
                  extendSearchTerm = true;
                  break;
              }
              break;
            case 'value':
              context.scope = this.isFunction(currentToken)
                ? this.scopeAfterFunction(currentToken, context.field)
                : 'operator';
              break;
            case 'list-value':
              if (currentToken.endsWith(')')) {
                context.scope = 'operator';
              } else {
                extendSearchTerm = true;
              }
              break;
            case 'quoted-value':
              if (context.searchTerm.endsWith('"') && !context.searchTerm.endsWith('\\"')) {
                context.scope = 'operator';
              } else {
                extendSearchTerm = true;
              }
              break;
            case 'function':
              if (context.searchTerm.endsWith(")")) {
                context.scope = this.scopeAfterFunction(context.searchTerm, context.field);
              } else {
                extendSearchTerm = true;
              }
              break;
            case 'operator':
              context.scope = 'field';
              context.field = null;
              context.model = this.baseModel;
              break;
          }
          context.searchTerm = extendSearchTerm
            ? context.searchTerm + ' ' + currentToken
            : currentToken;
          extendSearchTerm = false;
        } while (!!rest);

        context.searchTerm = trimStart(context.searchTerm, '"(');
        if (context.scope === "list-value") {
          context.searchTerm = context.searchTerm.split(",").slice(-1)[0].trim();
        }

        if (context.scope === "field") {
          context.model = this.getModelFromPath(context.searchTerm);
          context.searchTerm = context.searchTerm.split(this.schema["path_separator"]).slice(-1)[0];
        }

        if (context.field !== null) {
          context.model = this.getModelFromPath(context.field);
          context.field = context.field.split(this.schema["path_separator"]).slice(-1)[0];
        }

        return context;
      },

      getFieldNamesOf: function (model) {
        return Object.getOwnPropertyNames(this.schema[model]["fields"]);
      },

      getModelFromPath: function (path) {
        path = Array.isArray(path) ? path : path.split(this.schema["path_separator"]).slice(0, -1);
        return path.reduce(function (model, field) {
          // TODO: error handling: invalid model or invalid field (wrong name or not a relation)
          return this.schema[model]["fields"][field]["related"];
        }.bind(this), this.baseModel);
      },

      getFnSuggestion: function (fnName, fnMeta) {
        const suffix = fnMeta["params"].length ? '(' : '()';
        return new Suggestion(fnName + suffix, fnName, fnMeta["help"])
      },

      suggestFor: function (expression) {
        var execFn = function (resolve, reject) {
          var context = this.getContext(expression);
          var suggestions = [];

          switch (context.scope) {
            case 'field':
              const exactMatch = this.schema[context.model]["fields"][context.searchTerm];
              if (exactMatch !== undefined && exactMatch["related"]) {
                suggestions.push(new Suggestion(
                  context.searchTerm + ".",
                  context.searchTerm + ".",
                  "Filter by " + exactMatch["related"].split(".")[1] + " attributes")
                );
              }

              Object.keys(this.schema[context.model]["fields"])
                .forEach((field) => {
                  const fieldSchema = this.schema[context.model]["fields"][field];
                  const suffix = fieldSchema.related && exactMatch === undefined ? "" : " ";
                  const help = fieldSchema.search_url ? "Search for " + field : "";
                  suggestions.push(new Suggestion(field + suffix, field, help));
                  if (fieldSchema['type'] === "boolean") {
                    suggestions.push(
                      new Suggestion('is ' + field + suffix, 'is ' + field)
                    );
                    suggestions.push(
                      new Suggestion(
                        'is not ' + field + suffix, 'is not ' + field
                      )
                    );
                  }
                });

                const functions = {
                  ...this.schema[context.model]["functions"],
                  ...this.schema["common_functions"]
                };
                Object.keys(functions).forEach(function (fnName) {
                  const fnMeta = functions[fnName];
                  if (fnMeta["role"] !== "value") {
                    suggestions.push(this.getFnSuggestion(fnName, fnMeta));
                  }
                }.bind(this));
              break;
            case 'lookup':
              suggestions = this.lookupSuggestions;
              break;
            case 'value':
            case 'list-value':
            case 'quoted-value':
              const suffix = context.scope === 'list-value' ? ', ' : ' ';
              const field = this.schema[context.model]["fields"][context.field];
              if (field.choices) {
                field.choices.forEach((choice) => {
                  suggestions.push(new Suggestion(choice + suffix, choice));
                });
              } else if (field.type === "boolean") {
                suggestions = this.booleanSuggestions;
              } else if (field.search_url) {
                this.fetchRelated(field, context.searchTerm)
                  .then((res) => {
                    const objects = this.getObjects(res);
                    resolve(
                      objects.map(function (val) {
                        return this.mapToSuggestion(val, field, suffix);
                      }.bind(this))
                    );
                  })
                  .catch((err) => reject(err));
                return;
              } else {
                const functions = {
                  ...this.schema[context.model]["functions"],
                  ...this.schema["common_functions"]
                };
                Object.keys(functions).forEach(function (fnName) {
                  const fnMeta = functions[fnName];
                  if (fnMeta["role"] === "value") {
                    suggestions.push(this.getFnSuggestion(fnName, fnMeta));
                  }
                }.bind(this));
              }
              if (field.nullable) {
                suggestions.push(
                  new Suggestion(this.schema["empty_val"] + ' ', this.schema["empty_val"])
                );
              }
              break;
            case 'operator':
              suggestions = this.operatorSuggestions;
              break;
            case 'function':
              // TODO: suggestion for parameters
              break;
          }

          suggestions = context.searchTerm
            ? suggestions.filter((s) => s.display.startsWith(context.searchTerm))
            : suggestions;
          resolve(suggestions);
        }.bind(this);
        return new Promise(execFn);
      },

      mapToSuggestion: function (obj, field, suffix) {
        const value = obj[field['target_field']] + suffix;
        const display = this.optionDisplay === null ? value : this.optionDisplay(obj);
        const help = this.optionHelp === null ? '' : this.optionHelp(obj);
        return new Suggestion(value, display, help);
      },

      mergeSelection: function (value, selected) {
        const context = this.getContext(value);
        // just replace the search term we had with the selected value
        // the search term is assumed to be at the last position
        return value.slice(0, value.length - context.searchTerm.length) + selected;
      },

      setLoading: function (isLoading) {
        if (this.loading !== isLoading) {
          this.loading = isLoading;
          if (this.onloadingchange !== null) {
            this.onloadingchange(this.loading);
          }
        }
      },

      fetchSchema: function (url) {
        const schemaRequest = new XMLHttpRequest();
        schemaRequest.open('GET', url, true);

        schemaRequest.onreadystatechange = function () {
          if (schemaRequest.readyState === XMLHttpRequest.DONE) {
            if (schemaRequest.status === 200) {
              this.schema = JSON.parse(schemaRequest.responseText);
            } else {
              this.logger.error('Failed to fetch Django NLF schema from ' + url, schemaRequest);
            }
          }
        }.bind(this);

        schemaRequest.send();
      },

      fetchRelated: async function (field, searchTerm) {
        var execFn = function (resolve, reject) {
          if (this.ongoingRequest !== null) {
            this.ongoingRequest.abort();
          }

          this.ongoingRequest = new XMLHttpRequest();
          const url = field.search_url + '?' + field.search_param + '=' + encodeURIComponent(searchTerm);
          this.ongoingRequest.open('GET', url, true);

          this.ongoingRequest.onreadystatechange = function () {
            if (this.ongoingRequest.readyState === XMLHttpRequest.DONE) {
              this.setLoading(false);
              if (this.ongoingRequest.status === 200) {
                resolve(JSON.parse(this.ongoingRequest.responseText));
              } else {
                reject('Failed to fetch related objects from ' + url);
              }
              this.ongoingRequest = null;
            } else if (this.ongoingRequest.readyState === XMLHttpRequest.UNSENT) {
              reject('Fetch from ' + url + ' has been aborted!');
            }

          }.bind(this);

          this.setLoading(true);
          this.ongoingRequest.send();
        }.bind(this);
        return new Promise(execFn);
      }
    }

    return {
      Suggester: Suggester,
      OptionRenderer: null,
      Completion: null,
    };
  }
));
