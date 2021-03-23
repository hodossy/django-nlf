module.exports = function(config) {
  config.set({
    basePath: "",
    files: [
      // karma-jasmine-ajax seems to be outdated, hence the file
      // is included here
      {pattern: "node_modules/jasmine-ajax/lib/mock-ajax.js", watched: false},
      "django_nlf/static/django_nlf/js/suggestion.js",
      "django_nlf/static/django_nlf/js/autocomplete.js",
      "tests/javascripts/**/*.spec.js",
    ],
    frameworks: ["jasmine"],
    browsers: ["Chrome"],
    client: {
      clearContext: false, // leave Jasmine Spec Runner output visible in browser
    },
    reporters: ["progress", "kjhtml"],
    plugins: [
      "karma-chrome-launcher",
      "karma-jasmine",
      "karma-jasmine-html-reporter"
    ],
    singleRun: false,
    restartOnFileChange: true,
  });
};
