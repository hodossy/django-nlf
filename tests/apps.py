from django.apps import AppConfig


class DjangoNLFDemoAppConfig(AppConfig):
    name = "tests"
    verbose_name = "Django NLF Demo"

    def ready(self):
        from . import filter_functions
