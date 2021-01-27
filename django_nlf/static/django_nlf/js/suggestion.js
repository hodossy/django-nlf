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
    // Comming from the Django template tag
    var defaultOptions = JSON.parse(document.querySelector('#suggestionInit').textContent);

    function logError(msg) {
      console.log('DjangoNLF: ' + msg.toString());
    }

    function suggestion(value, display, help) {
      return {
        value: value,
        display: display,
        help: help || '',
      }
    }

    var Suggester = function(appLabel, model, options) {
      this.options = options || defaultOptions;
      this.schemaUrl = `${this.options.schemaRootUrl}/${appLabel}/${model}`;
      this.schema = null;
      this.schemaRequest = null;

      this.loading = false;
      this.onloadingchange = null;
      this.ongoingRequest = null;

      this.fetchSchema();
    }

    Suggester.prototype = {
      notSuggestion: suggestion('not ', 'not', ''),
      operatorSuggestions: [
        suggestion('and ', 'and', ''),
        suggestion('or ', 'or', ''),
        suggestion('not ', 'not', ''),
        suggestion('and not ', 'and not', ''),
        suggestion('or not ', 'or not', ''),
      ],
      lookupSuggestions: [
        suggestion('is ', 'is', ''),
        suggestion('is not ', 'is not', ''),
        suggestion('contains ', 'contains', ''),
        suggestion('does not contain ', 'does not contain', ''),
        suggestion('matches ', 'matches', ''),
        suggestion('does not match ', 'does not match', ''),
        suggestion('in ', 'in', ''),
        suggestion('not in ', 'not in', ''),
        suggestion('> ', 'greater than', ''),
        suggestion('>= ', 'greater than or equal', ''),
        suggestion('< ', 'lower than', ''),
        suggestion('<= ', 'lower than or equal', ''),
      ],
      depthRegex: /\./g,
      getContext: function(expression) {
        var context = {
          scope: null,
          field: null,
          searchTerm: null,
        };

        if (!expression) {
          context.scope = 'field';
          return context;
        }

        return context;
      },

      suggestFor: function (expression) {
        var execFn = function (resolve, reject) {
          var context = this.getContext();
          var suggestions = [];

          switch (context.scope) {
            case 'field':
              const depth = context.searchTerm
                ? (context.searchTerm.match(this.depthRegex) || []).length
                : 0;
              suggestions = this.schema.fields
                .filter((fieldSchema) => (fieldSchema.path.match(this.depthRegex) || []).length === depth)
                .map((fieldSchema) => {
                  const suffix = fieldSchema.search_url ? '' : ' ';
                  return suggestion(fieldSchema.path + suffix, fieldSchema.path);
                });
              break;
            case 'lookup':
              suggestions = context.searchTerm
              ? this.lookupSuggestions.filter((s) => s.display.startsWith(searchTerm))
              : this.lookupSuggestions;
              break;
            case 'value':
              if (context.field.choices) {
                suggestions = context.field.choices
                  .map((choice) => suggestion(choice + ' ', choice));
              } else if (context.field.search_url) {
                this.fetchRelated(field, context.searchTerm)
                  .then((res) => {
                    const objects = this.options.getObjects(res);
                    resolve(
                      objects.map(this.options.mapToSuggestion)
                    );
                  })
                  .catch((err) => reject(err));
                return;
              } else {
                suggestions = this.schema.functions.VALUE
                  .map((func) => {
                    const suffix = true ? '()' : '('; // TODO: check the number of parameters
                    return suggestion(func[0] + suffix, func[0], func[1]);
                  });
              }
              break;
            case 'operator':
              suggestions = this.operatorSuggestions;
              break;
          }

          suggestions = context.searchTerm
            ? suggestions.filter((s) => s.display.startsWith(searchTerm))
            : suggestions;
          resolve(suggestions);
        }.bind(this);
        return new Promise(execFn);
      },

      setLoading: function (isLoading) {
        if (this.loading !== isLoading) {
          this.loading = isLoading;
          if (this.onloadingchange !== null) {
            this.onloadingchange(this.loading);
          }
        }
      },

      fetchSchema: function () {
        this.schemaRequest = new XMLHttpRequest();
        this.schemaRequest.open('GET', this.schemaUrl, true);

        this.schemaRequest.onreadystatechange = function () {
          if (this.schemaRequest.readyState === XMLHttpRequest.DONE) {
            if (this.schemaRequest.status === 200) {
              this.schema = JSON.parse(this.schemaRequest.responseText);
            } else {
              logError('Failed to fetch Django NLF schema from ' + this.schemaUrl);
            }
            this.schemaRequest = null;
          }
        }.bind(this);

        this.schemaRequest.send();
      },

      fetchRelated: async function (field, searchTerm) {
        var execFn = function (resolve, reject) {
          var url, res;
          if (this.ongoingRequest !== null) {
            this.ongoingRequest.abort();
            resolve([]);
          }

          this.ongoingRequest = new XMLHttpRequest();
          url = field.search_url + '?' + field.search_param + '=' + searchTerm;
          this.ongoingRequest.open('GET', url, true);

          this.ongoingRequest.onreadystatechange = function () {
            if (this.ongoingRequest.readyState === XMLHttpRequest.DONE) {
              this.setLoading(false);
              if (this.ongoingRequest.status === 200) {
                res = JSON.parse(this.ongoingRequest.responseText);
                resolve(res);
              } else {
                reject('Failed to fetch related objects: ' + field.path);
              }
              this.ongoingRequest = null;
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
