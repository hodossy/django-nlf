describe('OptionRenderer', () => {
  var input, wrapper, renderer;
  var options = {
    selector: '#testContainer input',
  };
  var testOptions = [
    {
      value: '',
      display: 'Option 0',
      help: 'help'
    },
    {
      value: '',
      display: 'Option 1',
      help: ''
    },
    {
      value: '',
      display: 'Option 2',
    },
  ]

  beforeAll(() => {
    wrapper = document.createElement('div');
    wrapper.id = "testContainer";
    input = document.createElement('input');
    wrapper.appendChild(input);
    document.body.appendChild(wrapper);
  });

  beforeEach(() => {
    renderer = new DjangoNLF.OptionRenderer(options);
  });

  afterEach(() => {
    renderer.optionContainer.remove();
    renderer = null;
  });

  afterAll(() => {
    wrapper.remove();
    wrapper = input = null;
  });

  it('should be defined', () => {
    expect(DjangoNLF.OptionRenderer).toBeDefined();
  });

  describe('initOptionContainer()', () => {
    it('should create a wrapper element', () => {
      expect(renderer.optionContainer).toBeDefined();
      expect(renderer.optionContainer.children[0]).toBeDefined();
    });

    it('should add css classes', () => {
      const containerClasses = renderer.optionContainer.classList;
      expect(containerClasses.contains(renderer.blockName)).toBeTruthy();
      expect(containerClasses.contains(renderer.blockHiddenClass)).toBeTruthy();

      const listClasses = renderer.optionContainer.children[0].classList;
      expect(listClasses.contains(renderer.optionListClass)).toBeTruthy();
    });
  });


  describe('createOption()', () => {
    var li;

    beforeEach(() => {
      li = renderer.createOption();
    });

    it('should create an option element', () => {
      expect(li.classList.contains(renderer.optionClass)).toBeTruthy();
      expect(li.children.length).toEqual(2);
      expect(li.onclick).toBeDefined();
    });

    it('should add to the option list', () => {
      expect(li).toBe(renderer.optionList.children[0]);
    });
  });

  describe('showPanel()', () => {
    beforeEach(() => {
      renderer.showPanel();
    });

    it('should remove the hidden class', () => {
      const containerClasses = renderer.optionContainer.classList;
      expect(containerClasses.contains(renderer.blockHiddenClass)).toBeFalsy();
    });

    it('should position the container', () => {
      const containerStyle = renderer.optionContainer.style;
      expect(containerStyle.left).toBeDefined();
      expect(containerStyle.top).toBeDefined();
      expect(containerStyle.width).toBeDefined();
    });
  });

  describe('hidePanel()', () => {
    beforeEach(() => {
      renderer.showPanel();
    });

    it('should add the hidden class', () => {
      renderer.hidePanel();
      const containerClasses = renderer.optionContainer.classList;
      expect(containerClasses.contains(renderer.blockHiddenClass)).toBeTruthy();
    });
  });

  describe('onClick()', () => {
    beforeEach(() => {
      renderer.render(testOptions);
    });

    it('should select the clicked element', (done) => {
      renderer.optionElements[2].dispatchEvent(new Event('click'));
      setTimeout(() => {
        expect(renderer.selected).toEqual(2);
        done();
      })
    });

    it('should call onOptionClicked if defined', (done) => {
      renderer.onOptionClicked = () => {
        expect(true).toBeTruthy();  // supress spec has no expectation warning
        done();
      };
      renderer.optionElements[2].dispatchEvent(new Event('click'));
    }, 10);
  });

  describe('select(index)', () => {
    beforeEach(() => {
      renderer.autoselectFirst = true;
      renderer.render(testOptions);
    });

    it('should clear selection for null', () => {
      renderer.select(null);
      for (option of renderer.optionElements) {
        expect(option.classList.contains(renderer.optionActiveClass)).toBeFalsy();

      }
    });

    it('should add class to the selected option', () => {
      expect(renderer.optionElements[0].classList.contains(renderer.optionActiveClass)).toBeTruthy();
    });

    it('should remove class from the prev selected option', () => {
      renderer.select(1);
      expect(renderer.optionElements[0].classList.contains(renderer.optionActiveClass)).toBeFalsy();
    });

    it('should select the last option for too large indices', () => {
      renderer.select(42);
      expect(renderer.optionElements[2].classList.contains(renderer.optionActiveClass)).toBeTruthy();
    });

    it('should select the first option for negative indices', () => {
      renderer.select(-1);
      expect(renderer.optionElements[0].classList.contains(renderer.optionActiveClass)).toBeTruthy();
    });

    it('should scroll to the selection', () => {
      const scrollToSelectionSpy = spyOn(renderer, 'scrollToSelection');
      renderer.select(1);
      expect(scrollToSelectionSpy).toHaveBeenCalled();
    });
  });

  describe('scrollToSelection()', () => {
    beforeEach(() => {
      renderer.optionContainer.style.maxHeight = '36px';
      renderer.optionContainer.style.overflow = 'auto';
      renderer.optionList.style.padding = '0px';
      renderer.optionList.style.margin = '0px';
      renderer.autoselectFirst = true;
      renderer.render(testOptions);
    });

    it('should do nothing when there is no scrollbar', () => {
      renderer.optionContainer.style.maxHeight = '100px';
      renderer.select(1);
      expect(renderer.optionContainer.scrollTop).toEqual(0);
    });

    it('should do not scroll when the selected option is visible', () => {
      renderer.select(1);
      expect(renderer.optionContainer.scrollTop).toEqual(0);
    });

    it('should scroll down when the selected option is below the visible area', () => {
      renderer.select(2);
      expect(renderer.optionContainer.scrollTop).toEqual(18);
    });

    it('should scroll up when the selected option is below the visible area', () => {
      renderer.select(2);
      expect(renderer.optionContainer.scrollTop).toEqual(18);

      renderer.select(0);
      expect(renderer.optionContainer.scrollTop).toEqual(0);
    });
  });

  describe('getSelectedValue()', () => {
    it('should return null when there is no selection', () => {
      expect(renderer.getSelectedValue()).toBeNull();
    });

    it('should return the value of selection', () => {
      renderer.render(testOptions);
      expect(renderer.getSelectedValue()).toEqual('');
    });
  });

  describe('render', () => {
    it('should create new option elements if needed', () => {
      const createOptionSpy = spyOn(renderer, 'createOption').and.callThrough();
      renderer.render(testOptions);

      expect(createOptionSpy).toHaveBeenCalledTimes(3);
    });

    it('should remove old option elements when not used any more', () => {
      renderer.render(testOptions);

      const removeChildSpy = spyOn(renderer.optionList, 'removeChild').and.callThrough();
      renderer.render(testOptions.slice(0, 1));

      expect(removeChildSpy).toHaveBeenCalledTimes(2);
    });

    it('should show the panel when there are options', () => {
      const showPanelSpy = spyOn(renderer, 'showPanel').and.callThrough();
      renderer.render(testOptions);

      expect(showPanelSpy).toHaveBeenCalled();
    });

    it('should auto-select the first option if enabled', () => {
      const selectSpy = spyOn(renderer, 'select').and.callThrough();
      renderer.render(testOptions);

      expect(selectSpy).toHaveBeenCalledWith(0);
    });

    it('should not select the first option if disabled', () => {
      const selectSpy = spyOn(renderer, 'select').and.callThrough();
      renderer.autoselectFirst = false;
      renderer.render(testOptions);

      expect(selectSpy).not.toHaveBeenCalled();
    });
  });
});
