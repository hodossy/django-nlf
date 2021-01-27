(function (root) {
  if (root.DjangoNLF === undefined) {
    return;
  }
  var Completion = function (appLabel, model, options) {
    this.input = document.querySelector(options.rendererOptions.selector);
    this.suggester = options.suggester || new root.DjangoNLF.Suggester(appLabel, model, options.suggetionOptions);
    this.renderer = options.renderer || new root.DjangoNLF.OptionRenderer(options.rendererOptions);

    this.input.addEventListener('keyup', function (e) {
      this.onKeyUp(e);
    }.bind(this));
  }

  Completion.prototype = {
    onKeyUp: function(e) {
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
        case 9:   // Tab
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

        default:
          this.suggester.suggestFor("").then(function (suggestions) {
            this.renderer.render(suggestions);
          }.bind(this));
      }
    }
  };

  this.DjangoNLF.Completion = Completion;
}(this))
