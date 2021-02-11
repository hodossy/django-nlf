describe('Completion', () => {
  var completion;
  var mockSuggester = {
    suggestFor: function (val) {return Promise.resolve([val])},
    mergeSelection: function (val, sel) { return val + sel; }
  };

  var mockRenderer = {
    getSelectedValue: function () { return 'bar'},
    selected: 0,
    select: function (index) {},
    showPanel: function () {},
    hidePanel: function () {},
    render: function () {},
    onOptionClicked: null,
  };

  var input = document.createElement('input');


  beforeEach(() => {
    completion = new DjangoNLF.Completion({
      renderer: mockRenderer,
      suggester: mockSuggester,
      input: input,
    })
  });

  afterEach(() => {
    mockRenderer.selected = 0;
  });

  it('should be defined', () => {
    expect(DjangoNLF.Completion).toBeDefined();
  });

  describe('constructor(options)', () => {
    it('should throw error on missing options', () => {
      expect(function () {new DjangoNLF.Completion()}).toThrow();
      expect(function () {new DjangoNLF.Completion({})}).toThrow();
    });

    it('should create with custom renderer/suggester', () => {
      expect(completion.renderer).toBe(mockRenderer);
      expect(completion.suggester).toBe(mockSuggester);
    });

    it('should create with default renderer/suggester', () => {
      const schemaUrl = '/schema';
      jasmine.Ajax.withMock(() => {
        jasmine.Ajax.stubRequest(schemaUrl).andReturn({
          status: 200,
          responseText: "{}",
        });
        const comp = new DjangoNLF.Completion({
          input: input,
          suggetionOptions: {
            schemaUrl: schemaUrl
          }
        });

        expect(comp.renderer).toEqual(jasmine.any(DjangoNLF.OptionRenderer));
        expect(comp.suggester).toEqual(jasmine.any(DjangoNLF.Suggester));
      });
    });

    it('should set onOptionClicked callback', () => {
      expect(completion.onOptionClicked).not.toBeNull();
    });

    it('should set up listeners', () => {
      expect(input.onkeydown).toBeDefined();
      expect(input.oninput).toBeDefined();
      expect(input.onfocus).toBeDefined();
      expect(input.onblur).toBeDefined();
    });
  });

  describe('onFocus(event)', () => {
    it('should trigger onInput', () => {
      const onInputSpy = spyOn(completion, 'onInput');
      completion.onFocus({target: {value: 'foo'}});

      expect(onInputSpy).toHaveBeenCalled();
    });

    it('should only show the panel when no input changed', () => {
      const showPanelSpy = spyOn(completion.renderer, 'showPanel');
      const onInputSpy = spyOn(completion, 'onInput');

      completion.lastValue = 'foo';
      completion.onFocus({target: {value: 'foo'}});
      expect(showPanelSpy).toHaveBeenCalled();
      expect(onInputSpy).not.toHaveBeenCalled();
    });
  });

  describe('onInput(event)', () => {
    beforeEach(() => {
      // uninstall befora install to avoid rare failure of install
      jasmine.clock().uninstall();
      jasmine.clock().install();
    });

    afterEach(() => {
      jasmine.clock().uninstall();
    });

    it('should render the suggestions', (done) => {
      const suggestForSpy = spyOn(completion.suggester, 'suggestFor').and.callThrough();
      const renderSpy = spyOn(completion.renderer, 'render');
      completion.onInput({target: {value: 'foo'}});
      jasmine.clock().tick(completion.debounce);
      expect(suggestForSpy).toHaveBeenCalledWith('foo');
      jasmine.clock().uninstall();
      // setTimeout needed to put expectation to the nex event loop
      // where our promise will be resolved
      setTimeout(() => {
        expect(renderSpy).toHaveBeenCalledWith(['foo']);
        done();
      });
    });

    it('should debounce the events', (done) => {
      const renderSpy = spyOn(completion.renderer, 'render');
      completion.onInput({target: {value: 'foo'}});
      completion.onInput({target: {value: 'bar'}});
      jasmine.clock().tick(completion.debounce);
      jasmine.clock().uninstall();
      // setTimeout needed to put expectation to the nex event loop
      // where our promise will be resolved
      setTimeout(() => {
        expect(renderSpy).toHaveBeenCalledOnceWith(['bar']);
        done();
      });
    });

    it('should store the last value', () => {
      completion.onInput({target: {value: 'foo'}});
      expect(completion.lastValue).toEqual('foo');

      completion.onInput({target: {value: 'bar'}});
      expect(completion.lastValue).toEqual('bar');
    });
  });

  describe('onKeyDown(upArrow)', () => {
    var e, selectSpy, preventDefaultSpy;

    beforeEach(() => {
      e = {keyCode: 38, preventDefault: null};
      selectSpy = spyOn(completion.renderer, 'select');
      preventDefaultSpy = spyOn(e, 'preventDefault');
    });

    it('should clear selection when the first option is selected', () => {
      completion.onKeyDown(e);
      expect(selectSpy).toHaveBeenCalledWith(null);
    });

    it('should prevent default', () => {
      completion.onKeyDown(e);
      expect(preventDefaultSpy).toHaveBeenCalled();
    });

    it('should do nothing if nothing is selected', () => {
      mockRenderer.selected = null;
      completion.onKeyDown(e);
      expect(selectSpy).not.toHaveBeenCalled();
      expect(preventDefaultSpy).not.toHaveBeenCalled();
    });

    it('should select the previous option', () => {
      mockRenderer.selected = 1;
      completion.onKeyDown(e);
      expect(selectSpy).toHaveBeenCalledWith(0);
    });
  });

  describe('onKeyDown(downArrow)', () => {
    var e, selectSpy, preventDefaultSpy;

    beforeEach(() => {
      e = {keyCode: 40, preventDefault: null};
      selectSpy = spyOn(completion.renderer, 'select');
      preventDefaultSpy = spyOn(e, 'preventDefault');
    });

    it('should prevent default', () => {
      completion.onKeyDown(e);
      expect(preventDefaultSpy).toHaveBeenCalled();
    });

    it('should select the first option if nothing is selected', () => {
      mockRenderer.selected = null;
      completion.onKeyDown(e);
      expect(selectSpy).toHaveBeenCalledWith(0);
    });

    it('should select the next option', () => {
      mockRenderer.selected = 1;
      completion.onKeyDown(e);
      expect(selectSpy).toHaveBeenCalledWith(2);
    });
  });

  [
    {name: "rightArrow", code: 39},
    {name: "enter", code: 13},
    {name: "tab", code: 9},
  ].forEach((testCase) => {
    describe(`onKeyDown(${testCase.name})`, () => {
      var e, completeInputSpy, preventDefaultSpy;

      beforeEach(() => {
        e = {keyCode: testCase.code, preventDefault: null};
        completeInputSpy = spyOn(completion, 'completeInput');
        preventDefaultSpy = spyOn(e, 'preventDefault');
      });

      it('should prevent default', () => {
        completion.onKeyDown(e);
        expect(preventDefaultSpy).toHaveBeenCalled();
      });

      it('should do nothing if nothing is selected', () => {
        mockRenderer.selected = null;
        completion.onKeyDown(e);
        expect(completeInputSpy).not.toHaveBeenCalled();
        expect(preventDefaultSpy).not.toHaveBeenCalled();
      });

      it('should complete the input', () => {
        completion.onKeyDown(e);
        expect(completeInputSpy).toHaveBeenCalled();
      });
    });
  });

  describe('onKeyDown(esc)', () => {
    var e, selectSpy, preventDefaultSpy;

    beforeEach(() => {
      e = {keyCode: 27, preventDefault: null};
      hidePanelSpy = spyOn(completion.renderer, 'hidePanel');
      preventDefaultSpy = spyOn(e, 'preventDefault');
    });

    it('should prevent default if there is a panel shown', () => {
      hidePanelSpy.and.returnValue(true);
      completion.onKeyDown(e);
      expect(preventDefaultSpy).toHaveBeenCalled();
    });

    it('should not prevent default if there is no panel shown', () => {
      completion.onKeyDown(e);
      expect(preventDefaultSpy).not.toHaveBeenCalled();
    });

    it('should hide the panel', () => {
      completion.onKeyDown(e);
      expect(hidePanelSpy).toHaveBeenCalled();
    });
  });

  describe('completeInput()', () => {
    it('should merge the current value with the selected value', () => {
      completion.input.value = 'foo';

      completion.completeInput();
      expect(completion.input.value).toEqual('foobar');
    });

    it('should trigger an onInput', () => {
      const onInputSpy = spyOn(completion, 'onInput');
      completion.input.value = 'foo';

      completion.completeInput();
      expect(onInputSpy).toHaveBeenCalled();
    });
  });
});
