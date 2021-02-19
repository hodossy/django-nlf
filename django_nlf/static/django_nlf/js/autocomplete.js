(function (root) {
  if (root['DjangoNLF'] === undefined) {
    return;
  }

  function checkInput(input) {
    if (input === null) {
      throw new Error("Either 'input' or 'selector' must be defined!");
    }
  }

  var OptionRenderer = function(options) {
    this.autoselectFirst = options['autoselectFirst'] || true;
    this.input = options['input'] || document.querySelector(options['selector']);
    checkInput(this.input);

    this.optionElements = [];
    this.onOptionClicked = null;
    this.selected = null;
    this.suggestions = [];

    this.initOptionContainer();
  };

  OptionRenderer.prototype = {
    optionContainer: null,
    optionList: null,
    blockName: 'nlf-autocomplete',
    blockHiddenClass: 'nlf-autocomplete--hidden',
    optionClass: 'nlf-autocomplete__option',
    optionActiveClass: 'nlf-autocomplete__option--active',
    optionListClass: 'nlf-autocomplete__list',
    optionValueClass: 'nlf-autocomplete__value',
    optionHintClass: 'nlf-autocomplete__hint',

    initOptionContainer: function () {
      this.optionContainer = document.createElement('div');
      this.optionContainer.classList.add(this.blockName);
      this.optionContainer.classList.add(this.blockHiddenClass);

      this.optionList = document.createElement('ul');
      this.optionList.classList.add(this.optionListClass);
      this.optionContainer.appendChild(this.optionList);

      document.body.appendChild(this.optionContainer);
    },

    render: function (suggestions) {
      this.suggestions = suggestions;

      for (var i = 0; i < this.suggestions.length; i++) {
        // make sure we have enough li elements
        if (this.optionElements[i] == undefined) {
          this.optionElements[i] = this.createOption();
        }

        const suggestion = this.suggestions[i];
        this.optionElements[i].children[0].innerText = suggestion['display'];
        this.optionElements[i].children[1].innerText = suggestion['help'] || "";
        this.optionElements[i].children[1].title = suggestion['help'] || "";
      }

      for (var i = this.optionElements.length - 1; i >= this.suggestions.length; i--) {
        // remove not used li, if any
        this.optionList.removeChild(this.optionElements.pop());
      }

      if (this.suggestions.length) {
        this.showPanel();
        if (this.autoselectFirst) {
          this.select(0);
        }
      } else {
        this.hidePanel();
      }
    },

    createOption: function () {
      const li = document.createElement('li');
      li.classList.add(this.optionClass);
      li.onclick = function (e) {
        this.onClick(e);
      }.bind(this);

      li.appendChild(this.createOptionContent());
      li.appendChild(this.createOptionContent(true));

      this.optionList.appendChild(li);
      return li;
    },

    createOptionContent: function(isHint) {
      const span = document.createElement('span');
      span.classList.add(isHint ? this.optionHintClass : this.optionValueClass);
      return span;
    },

    showPanel: function () {
      const rect = this.input.getBoundingClientRect();
      this.optionContainer.style.position = 'absolute';
      this.optionContainer.style.left = `${rect.left}px`;
      this.optionContainer.style.top = `${rect.top + rect.height}px`;
      this.optionContainer.style.width = `${rect.width}px`;

      this.optionContainer.classList.remove(this.blockHiddenClass);
    },

    hidePanel: function () {
      if (!this.optionContainer.classList.contains(this.blockHiddenClass)) {
        this.optionContainer.classList.add(this.blockHiddenClass);
        return true;
      }
      return false;
    },

    onClick: function (e) {
      const optionIndex = this.optionElements.indexOf(e.target);
      this.select(optionIndex);
      if (this.onOptionClicked !== null) {
        this.onOptionClicked();
      }
    },

    select: function (index) {
      if (this.selected !== null && this.optionElements[this.selected] !== undefined) {
        this.optionElements[this.selected].classList.remove(this.optionActiveClass);
      }
      if (index != null) {
        this.selected = Math.min(Math.max(0, index), this.optionElements.length - 1);
        this.optionElements[this.selected].classList.add(this.optionActiveClass);
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
  OptionRenderer.prototype.constructor = OptionRenderer;

  var Completion = function (options) {
    if (options === undefined) {
      // TODO: documentation link to available options
      throw Error("Mandatory options must be defined! See the documentation!");
    }

    this.suggester = options['suggester'] || this.getDefaultSuggester(options);
    this.renderer = options['renderer'] || this.getDefaultRenderer(options);
    this.renderer.onOptionClicked = function () {
      this.completeInput();
    }.bind(this);

    this.debounce = options['debounce'] || 225;
    this.inputDebounceTimer = null;

    this.lastValue = null;
    this.input = options['input'] || document.querySelector(options['selector']);
    checkInput(this.input);
    this.setUpListeners();
  }

  Completion.prototype = {
    getDefaultSuggester: function (options) {
      const suggestionOptions = options['suggestionOptions'] || {};
      return new root.DjangoNLF.Suggester(suggestionOptions);
    },

    getDefaultRenderer: function (options) {
      const rendererOptions = options['rendererOptions'] || {};
      rendererOptions['input'] = options['input'];
      rendererOptions['selector'] = options['selector'];
      return new OptionRenderer(rendererOptions);
    },

    setUpListeners: function () {
      this.input.addEventListener('keydown', function (e) {
        this.onKeyDown(e);
      }.bind(this));
      this.input.addEventListener('input', function (e) {
        this.onInput(e);
      }.bind(this));
      this.input.addEventListener('focus', function (e) {
        this.onFocus(e);
      }.bind(this));
      this.input.addEventListener('blur', function () {
        this.renderer.hidePanel();
      }.bind(this));
    },

    onFocus: function(e) {
      // prevent the re-render of the same options,
      // it could be expensive for relations
      if (this.lastValue === e.target.value) {
        this.renderer.showPanel();
      } else {
        this.onInput(e);
      }
    },

    onInput: function (e) {
      if (this.inputDebounceTimer) {
        clearTimeout(this.inputDebounceTimer);
        this.inputDebounceTimer = null;
      }

      this.lastValue = e.target.value;
      this.inputDebounceTimer = setTimeout(function () {
        this.suggester.suggestFor(this.lastValue).then(function (suggestions) {
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
        case 13:  // Enter
        case 9:   // Tab, may not be a good idea for accessibility
          if (this.renderer.selected !== null) {
            this.completeInput();
            e.preventDefault();
          }
          break;

        case 27:  // Esc
          // Esc clears the selection for input[type='search']
          // we intend to keep that functionality
          if (this.renderer.hidePanel()) {
            e.preventDefault();
          };
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
  Completion.prototype.constructor = Completion;

  root['DjangoNLF']['OptionRenderer'] = OptionRenderer;
  root['DjangoNLF']['Completion'] = Completion;
}(this))
