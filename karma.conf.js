module.exports = function(config) {
  config.set({
    basePath: "",
    files: [
      "django_nlf/static/django_nlf/js/suggestion.js",
      "django_nlf/static/django_nlf/js/autocomplete.js",
      "tests/javascripts/**/*.spec.js",
    ],
    frameworks: ["jasmine"],
    browsers: ["Chrome", "ChromeCI"],
    client: {
      clearContext: false, // leave Jasmine Spec Runner output visible in browser
    },
    reporters: ["dots", "kjhtml"],
    plugins: [
      "karma-chrome-launcher",
      "karma-jasmine",
      "karma-jasmine-html-reporter"
    ],
    customLaunchers: {
      ChromeCI: {
        base: "ChromeHeadless",
        flags: ["--no-sandbox"],
      },
    },
    singleRun: false,
    restartOnFileChange: true,
  });
};
