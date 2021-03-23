module.exports = function(config) {
  config.set({
    basePath: "",
    files: [
      {pattern: "node_modules/jasmine-ajax/lib/mock-ajax.js", watched: false},
      "django_nlf/static/django_nlf/js/suggestion.js",
      "django_nlf/static/django_nlf/js/autocomplete.js",
      "tests/javascripts/**/*.spec.js",
    ],
    preprocessors: {
      "django_nlf/**/*.js": ["coverage"]
    },
    frameworks: ["jasmine"],
    browsers: ["ChromeCI"],
    reporters: ["dots", "coverage"],
    coverageReporter: {
      reporters: [
        { type: "text" },
        { type: "text-summary" },
      ]
    },
    plugins: [
      "karma-chrome-launcher",
      "karma-jasmine",
      "karma-coverage",
    ],
    customLaunchers: {
      ChromeCI: {
        base: "ChromeHeadless",
        flags: ["--no-sandbox"],
      },
    },
    singleRun: true,
    restartOnFileChange: false,
  });
};
