DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    },
}

INSTALLED_APPS = (
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django.contrib.auth",
    "django_nlf",
    "rest_framework",
    "tests.apps.DjangoNLFDemoAppConfig",
)

MIDDLEWARE = []

SECRET_KEY = "foobar"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    }
]

STATIC_URL = "/static/"

ROOT_URLCONF = "tests.urls"
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
DEBUG = True

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": (
        "django_nlf.rest_framework.DjangoNLFilterBackend",
        "rest_framework.filters.SearchFilter",
    ),
    "TEST_REQUEST_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.TemplateHTMLRenderer",
    ),
}
