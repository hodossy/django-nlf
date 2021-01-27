(function (root) {
  if (root.DjangoNLF === undefined) {
    return;
  }
  var OptionRenderer = function(options) {
    this.input = document.querySelector(options.selector);
    this.autoselectFirst = options.autoselectFirst || true;
    this.selected = null;
    this.onselect = options.onselect || null;

    this.suggestions = [];
    this.optionElements = [];
    this.initOptionContainer();
  };

  OptionRenderer.prototype = {
    optionContainer: null,
    optionList: null,
    initOptionContainer: function () {
      this.optionContainer = document.createElement('div');
      this.optionContainer.className = 'nlf-autocomplete nlf-autocomplete--hidden';

      this.optionList = document.createElement('ul');
      this.optionList.className = 'nlf-autocomplete__list';
      this.optionContainer.appendChild(this.optionList);

      document.body.appendChild(this.optionContainer);
    },
    render: function (suggestions) {
      this.suggestions = suggestions;

      for (var i = 0; i < this.suggestions.length; i++) {
        // make sure we have enough li elements
        if (this.optionElements[i] === undefined) {
          this.optionElements[i] = this.createOptionLi();
        }

        const suggestion = this.suggestions[i];
        this.optionElements[i].children[0].innerText = suggestion.display;
        if (suggestion.help) {
          this.optionElements[i].children[1].innerText = suggestion.help;
          this.optionElements[i].children[1].title = suggestion.help;
        }
      }

      for (var i = this.suggestions.length; i < this.optionElements.length; i++) {
        // remove not used li, if any
        this.optionList.removeChild(this.optionElements[i]);
        delete this.optionElements[i];
      }

      if (this.autoselectFirst) {
        this.select(0);
      }

      this.showPanel();
    },
    createOptionLi: function () {
      const li = document.createElement('li');
      li.className = 'nlf-autocomplete__option';

      li.appendChild(this.createOptionSpan('value'));
      li.appendChild(this.createOptionSpan('hint'));

      this.optionList.appendChild(li);
      return li
    },
    createOptionSpan: function(role) {
      const span = document.createElement('span');
      span.className = `nlf-autocomplete__${role}`;
      return span;
    },
    showPanel: function () {
      const rect = this.input.getBoundingClientRect();
      this.optionContainer.style.left = `${rect.left}px`;
      this.optionContainer.style.top = `${rect.top + rect.height}px`;
      this.optionContainer.style.width = `${rect.width}px`;

      if (this.optionContainer.className.includes('hidden')) {
        this.optionContainer.className = 'nlf-autocomplete';
      }
    },
    hidePanel: function () {
      if (!this.optionContainer.className.includes('hidden')) {
        this.optionContainer.className += ' nlf-autocomplete--hidden';
      }
    },
    select: function (index) {
      if (this.selected !== null) {
        this.optionElements[this.selected].className = 'nlf-autocomplete__option';
      }
      if (index != null) {
        this.selected = Math.min(Math.max(0, index), this.optionElements.length);
        this.optionElements[this.selected].className += ' nlf-autocomplete__option--active';
      } else {
        this.selected = null;
      }
    },
    getSelected: function () {
      return this.selected === null ? null : this.suggestions[this.selected];
    }
  };

  root.DjangoNLF.OptionRenderer = OptionRenderer;
}(this))
