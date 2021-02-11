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
        new Suggestion('is ', 'is', ''),
        new Suggestion('is not ', 'is not', ''),
        new Suggestion('contains ', 'contains', ''),
        new Suggestion('does not contain ', 'does not contain', ''),
        new Suggestion('matches ', 'matches', ''),
        new Suggestion('does not match ', 'does not match', ''),
        new Suggestion('in (', 'in', ''),
        new Suggestion('not in (', 'not in', ''),
        new Suggestion('> ', 'greater than', ''),
        new Suggestion('>= ', 'greater than or equal', ''),
        new Suggestion('< ', 'lower than', ''),
        new Suggestion('<= ', 'lower than or equal', ''),
      ],
      depthRegex: /\./g,
      fnRegex: /\w+\(/,

      isBooleanShortcut: function(field) {
        if (!field.startsWith("is")) {
          return false;
        }
        const fieldPath = field.slice(2).toLowerCase();
        return this.schema['fields'].filter((f) => {
          return f['type'] === "boolean" && f['path'] === fieldPath;
        }).length === 1;
      },

      isFunction: function(value) {
        const match = value.match(this.fnRegex);
        return match && match.length > 0;
      },

      scopeAfterFunction: function(value) {
        const openParenIndex = value.indexOf("(");
        if ( openParenIndex > 0 && value.indexOf(")") === -1) return 'function';

        const fnName = value.substr(0, openParenIndex);
        const fn = this.schema['functions'].filter((fn) => {
          return fn['name'] === fnName;
        })[0];

        if (fn['role'] === "field") return "lookup";
        // value and expression functions
        return "operator";
      },

      checkLookup: function (value) {
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
              context.field = context.searchTerm.startsWith('(')
                ? context.searchTerm.slice(1)
                : context.searchTerm;
              context.scope = this.isBooleanShortcut(context.field) ? 'operator' : 'lookup';
              break;
            case 'lookup':
              switch (this.checkLookup(context.searchTerm)) {
                case 'full':
                  if (context.searchTerm === 'is' && currentToken === 'not') {
                    extendSearchTerm = true;
                  } else {
                    context.scope = this.isFunction(currentToken)
                    ? this.scopeAfterFunction(currentToken)
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
                ? this.scopeAfterFunction(currentToken)
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
                context.scope = this.scopeAfterFunction(context.searchTerm);
              } else {
                extendSearchTerm = true;
              }
              break;
            case 'operator':
              context.scope = 'field';
              context.field = null;
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

        return context;
      },

      suggestFor: function (expression) {
        var execFn = function (resolve, reject) {
          var context = this.getContext(expression);
          var suggestions = [];

          switch (context.scope) {
            case 'field':
              let depth = context.searchTerm
                ? (context.searchTerm.match(this.depthRegex) || []).length
                : 0;

              const exactMatch = this.schema.fields
              .filter((fieldSchema) => (fieldSchema.path === context.searchTerm));
              if (exactMatch.length === 1) {
                depth += 1;
                suggestions.push(new Suggestion(exactMatch[0].path + ' ', exactMatch[0].path))
              }

              this.schema.fields
                .filter((fieldSchema) => (fieldSchema.path.match(this.depthRegex) || []).length === depth)
                .forEach((fieldSchema) => {
                  const suffix = fieldSchema.search_url ? '' : ' ';
                  suggestions.push(new Suggestion(fieldSchema.path + suffix, fieldSchema.path));
                });
              break;
            case 'lookup':
              suggestions = this.lookupSuggestions;
              break;
            case 'value':
            case 'list-value':
            case 'quoted-value':
              const suffix = context.scope === 'list-value' ? ', ' : ' ';
              const field = this.schema["fields"].find((f) => f["path"] === context.field);
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
                suggestions = this.schema.functions
                  .filter((func) => func["role"] === "value")
                  .map((func) => {
                    const suffix = func["params"].length ? '(' : '()';
                    return new Suggestion(func["name"] + suffix, func["name"], func["help"]);
                  });
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
                reject('Failed to fetch related ' + field.path + ' from ' + url);
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
