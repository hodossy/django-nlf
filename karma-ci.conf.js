module.exports = function(config) {
  config.set({
    basePath: "",
    files: [
      "django_nlf/static/django_nlf/js/suggestion.js",
      "django_nlf/static/django_nlf/js/autocomplete.js",
      "tests/javascripts/**/*.spec.js",
    ],
    frameworks: ["jasmine"],
    browsers: ["ChromeCI"],
    reporters: ["dots"],
    plugins: [
      "karma-chrome-launcher",
      "karma-jasmine",
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
