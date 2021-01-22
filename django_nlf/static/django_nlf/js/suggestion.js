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
      notSuggestion: { value: 'not ', display: 'not', help: '' },
      operatorSuggestions: [
        { value: 'and ', display: 'and', help: '' },
        { value: 'or ', display: 'or', help: '' },
        { value: 'not ', display: 'not', help: '' },
        { value: 'and not ', display: 'and not', help: '' },
        { value: 'or not ', display: 'or not', help: '' },
      ],
      lookupSuggestions: [
        { value: 'is ', display: 'is', help: '' },
        { value: 'is not ', display: 'is not', help: '' },
        { value: 'contains ', display: 'contains', help: '' },
        { value: 'does not contain ', display: 'does not contain', help: '' },
        { value: 'matches ', display: 'matches', help: '' },
        { value: 'does not match ', display: 'does not match', help: '' },
        { value: 'in ', display: 'in', help: '' },
        { value: 'not in ', display: 'not in', help: '' },
        { value: '> ', display: 'greater than', help: '' },
        { value: '>= ', display: 'greater than or equal', help: '' },
        { value: '< ', display: 'lower than', help: '' },
        { value: '<= ', display: 'lower than or equal', help: '' },
      ],
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
              break;
            case 'lookup':
              suggestions = context.searchTerm
              ? this.lookupSuggestions.filter((s) => s.display.startsWith(searchTerm))
              : this.lookupSuggestions;
              break;
            case 'value':
              if (context.field.choices) {
                suggestions = context.field.choices.map((choice) => {})
              } else if (context.field.search_url) {
                this.fetchRelated(field, context.searchTerm)
                  .then((res) => resolve(res))
                  .catch((err) => reject(err));
                return;
              }
              break;
            case 'operator':
              suggestions = context.searchTerm
                ? this.operatorSuggestions.filter((s) => s.display.startsWith(searchTerm))
                : this.operatorSuggestions;
              break;
          }

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
      Suggester: Suggester
    };
  }
));
