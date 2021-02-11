describe('Suggester', () => {
  const schemaUrl = "/api/schemas/tests/article";
  const testSchema = {
    fields: [{
      path: "id",
      type: "integer",
      help: "",
      nullable: false,
      choices: null,
      search_url: null,
      search_param: null,
      target_field: null
    }, {
      path: "archived",
      type: "boolean",
      help: "",
      nullable: false,
      choices: null,
      search_url: null,
      search_param: null,
      target_field: null
    }, {
      path: "headline",
      type: "string",
      help: "",
      nullable: true,
      choices: null,
      search_url: null,
      search_param: null,
      target_field: null
    }, {
      path: "publications",
      type: "integer",
      help: "",
      nullable: false,
      choices: null,
      search_url: "/publications/",
      search_param: "search",
      target_field: "id"
    },{
      path: "publications.subscription_fee",
      type: "number",
      help: "",
      nullable: false,
      choices: [1, 2, 3],
      search_url: null,
      search_param: null,
      target_field: null
    }, {
      path: "publications.articles",
      type: "integer",
      help: "",
      nullable: false,
      choices: null,
      search_url: "/articles/",
      search_param: "search",
      target_field: "id"
    }, {
      path: "publications.articles.id",
      type: "integer",
      help: "",
      nullable: false,
      choices: null,
      search_url: null,
      search_param: null,
      target_field: null
    }, {
      path: "publications.articles.headline",
      type: "string",
      help: "",
      nullable: false,
      choices: null,
      search_url: null,
      search_param: null,
      target_field: null
    }],
    functions: [
      { name: "fieldFn", role: "field", help: "", params: [] },
      { name: "valueFn", role: "value", help: "", params: [] },
      { name: "exprFn", role: "expression", help: "", params: [] },
    ],
    empty_val: "EMPTY"
  };
  var suggester;

  beforeEach(() => {
    jasmine.Ajax.install();

    jasmine.Ajax.stubRequest(schemaUrl).andReturn({
      status: 200,
      contentType: "application/json",
      responseText: "{}",
    });

    suggester = new DjangoNLF.Suggester({
      schemaUrl: schemaUrl,
    });
    suggester.schema = testSchema;
  });

  afterEach(() => {
    jasmine.Ajax.uninstall();
  });

  describe('constructor(options)', () => {
    it('should create with default options', () => {
      expect(suggester).toBeDefined();
    });
  });

  describe('getContext(expr)', () => {
    var expected;
    var generateTestCase = function (testCase) {
      it(`should be returned for '${testCase.expr}'`, () => {
        if (testCase.searchTerm) {
          expected.searchTerm = testCase.searchTerm;
        }
        if (testCase.field) {
          expected.field = testCase.field;
        }

        const res = suggester.getContext(testCase.expr);
        expect(res).toEqual(expected);
      });
    };

    describe('scope: field', () => {
      beforeEach(() => {
        expected = {
          scope: "field",
          field: null,
          searchTerm: "",
        }
      });

      [
        { expr: "" },
        { expr: "  " },
        { expr: "ar", searchTerm: "ar" },
        { expr: "archived", searchTerm: "archived" },
        { expr: "  ar", searchTerm: "ar" },
        { expr: "(" },
        { expr: "not (" },
        { expr: "isArchived and " },
        { expr: "exprFn() and " },
        { expr: 'exprFn(with, "two params") and ' },
        { expr: 'headline contains "some words" and ' },
        { expr: 'headline contains "some words" and id is not 12 or ' },
        { expr: '(headline contains "some words" and id is not 12) or ' },
        { expr: 'headline contains "some words" and (id is not 12 or ' },
        { expr: 'headline contains "some words" and (' },
      ].forEach(generateTestCase);
    });

    describe('scope: lookup', () => {
      beforeEach(() => {
        expected = {
          scope: "lookup",
          field: null,
          searchTerm: "",
        }
      });

      [
        { expr: "(archived ", field: "archived" },
        { expr: "not ( archived ", field: "archived" },
        { expr: "isArchived and headline co", searchTerm: "co", field: "headline" },
        { expr: "fieldFn() " },
        { expr: 'fieldFn(with, "two params") ' },
        { expr: 'headline contains "some words" and id ', field: "id" },
        { expr: 'headline contains "some words" and id does ', searchTerm: "does ", field: "id" },
        { expr: '(headline contains "some words" and id is not 12) or id ', field: "id" },
        { expr: 'headline contains "some words" and (id i', searchTerm: "i", field: "id" },
      ].forEach(generateTestCase);
    });

    describe('scope: value', () => {
      beforeEach(() => {
        expected = {
          scope: "value",
          field: null,
          searchTerm: "",
        }
      });

      [
        { expr: "(archived is ", field: "archived" },
        { expr: "not ( archived is not ", field: "archived" },
        { expr: "isArchived and headline contains foo", searchTerm: "foo", field: "headline" },
        { expr: "fieldFn() is " },
        { expr: 'fieldFn(with, "two params") is ' },
        { expr: 'headline contains "some words" and id is ', field: "id" },
        { expr: '(headline contains "some words" and id is not 12) or id is ', field: "id" },
        { expr: 'headline contains "some words" and (id is ', field: "id" },
      ].forEach(generateTestCase);
    });

    describe('scope: list-value', () => {
      beforeEach(() => {
        expected = {
          scope: "list-value",
          field: "id",
          searchTerm: "",
        }
      });

      [
        { expr: "id in (" },
        { expr: "id in (1", searchTerm: "1" },
        { expr: "id in (1," },
        { expr: "id in (1, " },
        { expr: "id in (1, 2", searchTerm: "2" },
      ].forEach(generateTestCase);
    });

    describe('scope: quoted-value', () => {
      beforeEach(() => {
        expected = {
          scope: "quoted-value",
          field: "headline",
          searchTerm: "",
        }
      });

      [
        { expr: 'headline contains "some', searchTerm: "some" },
        { expr: 'headline contains "some words', searchTerm: "some words" },
        { expr: 'headline contains "some escaped \\"quotes\\"', searchTerm: 'some escaped \\"quotes\\"' },
      ].forEach(generateTestCase);
    });

    describe('scope: function', () => {
      beforeEach(() => {
        expected = {
          scope: "function",
          field: null,
          searchTerm: "",
        }
      });

      [
        { expr: "exprFn(", searchTerm: "exprFn(" },
        { expr: "fieldFn(", searchTerm: "fieldFn(" },
        { expr: "id is valueFn(", field: "id", searchTerm: "valueFn(" },
      ].forEach(generateTestCase);
    });

    describe('scope: operator', () => {
      beforeEach(() => {
        expected = {
          scope: "operator",
          field: null,
          searchTerm: "",
        }
      });

      [
        { expr: "(archived is true a", searchTerm: "a", field: "archived" },
        { expr: "not ( archived is not true ", field: "archived" },
        { expr: "isArchived and headline contains foo ", field: "headline" },
        { expr: "exprFn() " },
        { expr: 'exprFn(with, "two params") ' },
        { expr: 'headline contains "some words" o', searchTerm: "o", field: "headline" },
        { expr: '(headline contains "some words" and id is not 12) ', field: "id" },
      ].forEach(generateTestCase);
    });
  });

  describe('suggestFor(expr)', () => {
    var getContextSpy, testContext;
    // actual call value does not matter, since
    // the context spy will decide what happens
    var expression = "";
    var generateTestCase = function (testCase) {
      it(`should suggest for "${testCase.searchTerm}"`, () => {
        testCase.searchTerm = testCase.searchTerm
        expect(res).toEqual(testCase.expected);
      });
    };

    beforeEach(() => {
      testContext = {
        scope: null,
        field: null,
        searchTerm: "",
      };
      getContextSpy = spyOn(suggester, "getContext");
    });

    describe('scope: field', () => {
      beforeEach(() => {
        testContext.scope = 'field';
      });

      it('should return all top level fields by default', () => {
        getContextSpy.and.returnValue(testContext);
        return suggester.suggestFor(expression).then((suggestions) => {
          expect(suggestions.length).toEqual(4);
          suggestions.forEach((sug) => {
            expect(sug.value.endsWith(" ")).toEqual(!sug.value.startsWith("pub"));
          });
        });
      });

      it('should filter top level fields by the search term', () => {
        testContext.searchTerm = "ar";
        getContextSpy.and.returnValue(testContext);
        return suggester.suggestFor(expression).then((suggestions) => {
          expect(suggestions.length).toEqual(1);
        });
      });

      it('should return the next level fields for a complete field', () => {
        testContext.searchTerm = "publications";
        getContextSpy.and.returnValue(testContext);
        return suggester.suggestFor(expression).then((suggestions) => {
          // first suggestion is itself with a space behind
          // to support searching for related items via API
          // the rest are the nested fields
          expect(suggestions.length).toEqual(3);
        });
      });

      it('should return the field for a complete field', () => {
        testContext.searchTerm = "publications";
        getContextSpy.and.returnValue(testContext);
        return suggester.suggestFor(expression).then((suggestions) => {
          expect(suggestions.length).toEqual(3);
          expect(suggestions[0].value.endsWith(" ")).toBeTrue();
        });
      });
    });

    describe('scope: lookup', () => {
      beforeEach(() => {
        testContext.scope = 'lookup';
      });

      it('should return all available lookups by default', () => {
        getContextSpy.and.returnValue(testContext);
        return suggester.suggestFor(expression).then((suggestions) => {
          expect(suggestions).toEqual(suggester.lookupSuggestions);
        });
      });

      it('should filter for the search term', () => {
        testContext.searchTerm = 'is';
        getContextSpy.and.returnValue(testContext);
        return suggester.suggestFor(expression).then((suggestions) => {
          expect(suggestions.length).toEqual(2);
        });
      });
    });

    describe('scope: value', () => {
      beforeEach(() => {
        testContext.scope = 'value';
      });

      it('should return choices of the field', () => {
        testContext.field = "publications.subscription_fee";
        getContextSpy.and.returnValue(testContext);
        return suggester.suggestFor(expression).then((suggestions) => {
          expect(suggestions.length).toEqual(3);
        });
      });

      it('should return true/false for boolean fields', () => {
        testContext.field = "archived";
        getContextSpy.and.returnValue(testContext);
        return suggester.suggestFor(expression).then((suggestions) => {
          expect(suggestions.length).toEqual(2);
        });
      });

      it('should return value functions when no better is available', () => {
        testContext.field = "headline";
        getContextSpy.and.returnValue(testContext);
        return suggester.suggestFor(expression).then((suggestions) => {
          expect(suggestions.length).toEqual(2);
          expect(suggestions[0].display.startsWith("value")).toBeTrue();
        });
      });

      it('should return the EMPTY value for nullable fields', () => {
        testContext.field = "headline";
        getContextSpy.and.returnValue(testContext);
        return suggester.suggestFor(expression).then((suggestions) => {
          expect(suggestions.length).toEqual(2);
          expect(suggestions[1].display.startsWith(testSchema.empty_val)).toBeTrue();
        });
      });

      it('should fetch suggestions from the API', () => {
        testContext.field = "publications";
        getContextSpy.and.returnValue(testContext);
        const fetchRelatedSpy = spyOn(suggester, "fetchRelated").and.returnValue(
          Promise.resolve({
            results: [
              {id: 1, title: "Publication 1"},
              {id: 2, title: "Publication 2"},
              {id: 3, title: "Publication 3"},
            ]
          })
        );

        return suggester.suggestFor(expression).then((suggestions) => {
          expect(suggestions.length).toEqual(3);
          suggestions.forEach((sug, idx) => {
            expect(sug.value).toEqual(`${idx + 1} `);
          })
        });
      });

      it('should use custom mappers for suggestions from the API', () => {
        testContext.field = "publications";
        getContextSpy.and.returnValue(testContext);
        const fetchRelatedSpy = spyOn(suggester, "fetchRelated").and.returnValue(
          Promise.resolve([
              {id: 1, title: "Publication 1"},
              {id: 2, title: "Publication 2"},
              {id: 3, title: "Publication 3"},
          ])
        );
        suggester.getObjects = (res) => res;
        suggester.optionDisplay = (obj) => obj.title;
        suggester.optionHelp = (obj) => `ID: ${obj.id}`;

        return suggester.suggestFor(expression).then((suggestions) => {
          expect(suggestions.length).toEqual(3);
          suggestions.forEach((sug, idx) => {
            expect(sug.value).toEqual(`${idx + 1} `);
            expect(sug.display).toEqual(`Publication ${idx + 1}`);
            expect(sug.help).toEqual(`ID: ${idx + 1}`);
          })
        });
      });
    });

    describe('scope: operator', () => {
      beforeEach(() => {
        testContext.scope = 'operator';
      });

      it('should return all available lookups by default', () => {
        getContextSpy.and.returnValue(testContext);
        return suggester.suggestFor(expression).then((suggestions) => {
          expect(suggestions).toEqual(suggester.operatorSuggestions);
        });
      });

      it('should filter for the search term', () => {
        testContext.searchTerm = 'an';
        getContextSpy.and.returnValue(testContext);
        return suggester.suggestFor(expression).then((suggestions) => {
          expect(suggestions.length).toEqual(2);
        });
      });
    });

    xdescribe('scope: function', () => {
      // TODO: suggestion for parameters
    });
  });

  describe('mergeSelection(value, selection)', () => {
    it('should cut the search term', () => {
      const getContextSpy = spyOn(suggester, "getContext").and.returnValue({searchTerm: "foo"})
      const res = suggester.mergeSelection("test is foo", "bar");
      expect(res).toEqual("test is bar");
    });
  });

  describe('setLoading(isLoading)', () => {
    it('should set the loading property', () => {
      suggester.setLoading(true);
      expect(suggester.loading).toBeTrue();
    });

    it('should call the onloadingchange callback when loading state changes', () => {
      const onLoadingChangedSpy = spyOn(suggester, 'onloadingchange');
      suggester.setLoading(true);
      expect(onLoadingChangedSpy).toHaveBeenCalled();
    });

    it('should not call the onloadingchange callback when loading state remains', () => {
      const onLoadingChangedSpy = spyOn(suggester, 'onloadingchange');
      suggester.setLoading(false);
      expect(onLoadingChangedSpy).not.toHaveBeenCalled();
    });
  });

  describe('fetchSchema()', () => {
    it('should parse the schema', (done) => {
      jasmine.Ajax.stubRequest("test").andReturn({
        status: 200,
        responseText: '{"foo": "bar"}'
      });

      suggester.fetchSchema("test");
      setTimeout(() => {
        expect(suggester.schema).toEqual({foo: "bar"});
        done();
      });
    });

    it('should log errors', (done) => {
      const errorSpy = spyOn(suggester.logger, "error");
      jasmine.Ajax.stubRequest("test").andReturn({
        status: 401,
        responseText: ''
      });

      suggester.fetchSchema("test");
      setTimeout(() => {
        expect(errorSpy).toHaveBeenCalled();
        done();
      });
    });
  });

  describe('fetchRelated(field, searchTerm)', () => {
    const testPublications = [
      {id: 0, title: 'Test publication 0'},
      {id: 1, title: 'Test publication 1'},
      {id: 2, title: 'Test publication 2'},
    ];

    it('should resolve with the response', () => {
      jasmine.Ajax.stubRequest("/publications/?search=foo").andReturn({
        status: 200,
        responseText: JSON.stringify({
          count: 3,
          next: null,
          previous: null,
          results: testPublications
        })
      });

      return suggester.fetchRelated(testSchema.fields[3], "foo").then((res) => {
        expect(res.count).toEqual(3);
        expect(res.results).toEqual(testPublications);
      });
    });

    it('should reject when an error happens', () => {
      jasmine.Ajax.stubRequest("/publications/?search=foo").andReturn({
        status: 500,
        responseText: null
      });

      return suggester.fetchRelated(testSchema.fields[3], "foo").catch((err) => {
        expect(err).toContain(testSchema.fields[3].path);
        expect(err).toContain(testSchema.fields[3].search_url);
        expect(err).toContain(testSchema.fields[3].search_param);
        expect(err).toContain("foo");
      });
    });

    it('should properly indicate loading state', (done) => {
      suggester.fetchRelated(testSchema.fields[3], "foo").then(() => {
        expect(suggester.loading).toBeFalse();
        done();
      });
      expect(suggester.loading).toBeTrue();

      jasmine.Ajax.requests.mostRecent().respondWith({
        status: 200,
        responseText: "[]"
      });
    });

    it('should cancel the previous pending request', (done) => {
      jasmine.Ajax.stubRequest("/publications/?search=foo").andReturn({
        status: 200,
        responseText: "[]"
      });
      var abortChecked = false;

      suggester.fetchRelated(testSchema.fields[3], "bar").catch((err) => {
        expect(err).toContain("bar");
        expect(err).toContain("aborted");
        abortChecked = true;
      });

      expect(jasmine.Ajax.requests.mostRecent().url).toContain("bar");

      suggester.fetchRelated(testSchema.fields[3], "foo").then(() => {
        expect(abortChecked).toBeTrue();
        done();
      });
    });
  });

});
