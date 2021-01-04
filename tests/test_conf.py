from unittest import TestCase

from django.test import override_settings

from django_nlf.conf import NLFSettings


class NLFSettingsTestCase(TestCase):
    def setUp(self):
        self.nlf_settings = NLFSettings()

    def test_retrieve_default(self):
        self.assertEqual(self.nlf_settings.EMPTY_VALUE, self.nlf_settings.DEFAULTS["EMPTY_VALUE"])

    @override_settings(NLF_EMPTY_VALUE="FOO")
    def test_retrieve_custom(self):
        self.assertEqual(self.nlf_settings.EMPTY_VALUE, "FOO")

    def test_invalid_setting(self):
        with self.assertRaises(AttributeError):
            self.nlf_settings.NON_EXISTING_SETTING  # pylint: disable=pointless-statement

    @override_settings(NLF_EMPTY_VALUE="FOO")
    def test_deprecated_setting(self):
        self.nlf_settings.DEPRECATED_SETTINGS = ["EMPTY_VALUE"]
        with self.assertWarns(DeprecationWarning):
            self.nlf_settings.EMPTY_VALUE  # pylint: disable=pointless-statement

    @override_settings(NLF_EMPTY_VALUE="django_nlf.utils.coerce_bool")
    def test_import_string(self):
        self.nlf_settings.IMPORT_STRINGS = "EMPTY_VALUE"
        self.assertTrue(callable(self.nlf_settings.EMPTY_VALUE))

    @override_settings(NLF_EMPTY_VALUE=("django_nlf.utils.coerce_bool",))
    def test_import_list(self):
        self.nlf_settings.IMPORT_STRINGS = ["EMPTY_VALUE"]
        self.assertEqual(len(self.nlf_settings.EMPTY_VALUE), 1)
        self.assertTrue(callable(self.nlf_settings.EMPTY_VALUE[0]))

    @override_settings(NLF_EMPTY_VALUE=True)
    def test_import_other(self):
        self.nlf_settings.IMPORT_STRINGS = ["EMPTY_VALUE"]
        self.assertEqual(self.nlf_settings.EMPTY_VALUE, True)

    @override_settings(NLF_EMPTY_VALUE="my.custom.module.function")
    def test_import_fail(self):
        self.nlf_settings.IMPORT_STRINGS = ["EMPTY_VALUE"]
        with self.assertRaises(ImportError):
            self.nlf_settings.EMPTY_VALUE  # pylint: disable=pointless-statement

    def test_settings_changed(self):
        self.nlf_settings.EMPTY_VALUE  # pylint: disable=pointless-statement
        self.assertTrue("EMPTY_VALUE" in self.nlf_settings.__dict__)
        self.nlf_settings.change_setting("RANDOM_SETTING", "FOO", True)
        self.nlf_settings.change_setting("NLF_RANDOM_SETTING", "FOO", True)
        self.assertTrue("EMPTY_VALUE" in self.nlf_settings.__dict__)
        self.nlf_settings.change_setting("NLF_EMPTY_VALUE", "FOO", True)
        self.assertFalse("EMPTY_VALUE" in self.nlf_settings.__dict__)
