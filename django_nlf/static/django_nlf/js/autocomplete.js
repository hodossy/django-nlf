(function (root) {
  if (root.DjangoNLF === undefined) {
    return;
  }
  var OptionRenderer = function(options) {
    this.autoselectFirst = options.autoselectFirst || true;
    this.input = document.querySelector(options.selector);
    this.onselect = options.onselect || null;

    this.optionElements = [];
    this.selected = null;
    this.suggestions = [];

    this.initOptionContainer();
  };

  OptionRenderer.prototype = {
    optionContainer: null,
    optionList: null,
    onOptionClicked: null,

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

      for (var i = this.optionElements.length - 1; i >= this.suggestions.length; i--) {
        // remove not used li, if any
        this.optionList.removeChild(this.optionElements.pop());
      }

      if (this.suggestions.length) {
        if (this.autoselectFirst) {
          this.select(0);
        }
        this.showPanel();
      } else {
        this.hidePanel();
      }
    },

    createOptionLi: function () {
      const li = document.createElement('li');
      li.className = 'nlf-autocomplete__option';
      li.onclick = function (e) {
        this.onClick(e);
      }.bind(this);

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

    onClick: function (e) {
      const optionIndex = this.optionElements.indexOf(e.target);
      this.select(optionIndex);
      if (this.onOptionClicked !== null) {
        this.onOptionClicked();
      }
    },

    select: function (index) {
      if (this.selected !== null) {
        this.optionElements[this.selected].className = 'nlf-autocomplete__option';
      }
      if (index != null) {
        this.selected = Math.min(Math.max(0, index), this.optionElements.length - 1);
        this.optionElements[this.selected].className += ' nlf-autocomplete__option--active';
        this.scrollToSelection();
      } else {
        this.selected = null;
      }

    },

    scrollToSelection: function () {
      if (this.optionContainer.clientHeight > this.optionContainer.scrollHeight) {
        return;
      }
      const minVisible = this.optionContainer.scrollTop;
      const maxVisible = minVisible + this.optionContainer.clientHeight;
      const selectedTop = this.optionElements[this.selected].offsetTop;
      const selectedBottom = selectedTop + this.optionElements[this.selected].scrollHeight;
      const currentScroll = this.optionContainer.scrollTop;
      if (selectedTop < minVisible) {
        // option is above the visible area
        this.optionContainer.scrollTop = currentScroll - (minVisible - selectedTop);
      }
      if (maxVisible < selectedBottom) {
        // option is below the visible area
        this.optionContainer.scrollTop = currentScroll + (selectedBottom - maxVisible);
      }
    },

    getSelectedValue: function () {
      return this.selected === null ? null : this.suggestions[this.selected].value;
    }
  };

  var Completion = function (appLabel, model, options) {
    this.suggester = options.suggester || new root.DjangoNLF.Suggester(appLabel, model, options.suggetionOptions);
    this.renderer = options.renderer || new OptionRenderer(options.rendererOptions);
    this.renderer.onOptionClicked = function () {
      this.completeInput();
    }.bind(this);
    this.debounce = options.debounce || 225;

    this.input = document.querySelector(options.rendererOptions.selector);
    this.input.addEventListener('keydown', function (e) {
      this.onKeyDown(e);
    }.bind(this));
    this.input.addEventListener('input', function (e) {
      this.onInput(e);
    }.bind(this));
    this.input.addEventListener('focus', function (e) {
      this.onInput(e);
    }.bind(this));
    this.input.addEventListener('blur', function () {
      this.renderer.hidePanel();
    }.bind(this));
  }

  Completion.prototype = {
    inputDebounceTimer: null,

    onInput: function (e) {
      if (this.inputDebounceTimer) {
        clearTimeout(this.inputDebounceTimer);
        this.inputDebounceTimer = null;
      }

      const val = e.target.value;
      this.inputDebounceTimer = setTimeout(function () {
        this.suggester.suggestFor(val).then(function (suggestions) {
          this.renderer.render(suggestions);
        }.bind(this));
      }.bind(this), this.debounce);
    },

    onKeyDown: function(e) {
      switch (e.keyCode) {
        case 38:  // up arrow
          if (this.renderer.selected !== null) {
            const newSelection = this.renderer.selected === 0
              ? null
              : this.renderer.selected - 1;
            this.renderer.select(newSelection);
            e.preventDefault();
          }
          break;

        case 40:  // down arrow
          const newSelection = this.renderer.selected === null
            ? 0
            : this.renderer.selected + 1;
          this.renderer.select(newSelection);
          e.preventDefault();
          break;

        case 39:  // right arrow
        case 9:   // Tab, may not be a good idea for accessibility
          if (this.renderer.selected !== null) {
            this.completeInput();
            e.preventDefault();
          }
          break;

        case 13:  // Enter
          if (this.renderer.selected !== null) {
            this.completeInput();
            e.preventDefault();
          }
          break;

        case 27:  // Esc
          this.renderer.hidePanel();
          break;

        case 16:  // Shift
        case 17:  // Ctrl
        case 18:  // Alt
        case 91:  // Windows Key or Left Cmd on Mac
        case 93:  // Windows Menu or Right Cmd on Mac
          // Control keys do not trigger panel popup
          break;
      }
    },

    completeInput: function () {
      const current = this.input.value;
      const selectedValue = this.renderer.getSelectedValue();
      this.input.value = this.suggester.mergeSelection(current, selectedValue);
      this.onInput({target: {value: this.input.value}});
    }
  };

  root.DjangoNLF.OptionRenderer = OptionRenderer;
  root.DjangoNLF.Completion = Completion;
}(this))
