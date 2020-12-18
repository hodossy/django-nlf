from unittest import TestCase

from django.test import override_settings

from django_nlf.utils import camel_to_snake_case, coerce_bool


class CamelToSnakeCaseTestCase(TestCase):
    def test_conversion(self):
        self.assertEqual(camel_to_snake_case("fooBar"), "foo_bar")
        self.assertEqual(camel_to_snake_case("_fooBar_"), "foo_bar_")
        self.assertEqual(camel_to_snake_case("HTTPRequest"), "h_t_t_p_request")


class CoerceBoolTestCase(TestCase):
    def test_with_default_settings(self):
        self.assertTrue(coerce_bool("true"))
        self.assertTrue(coerce_bool("a"))
        self.assertTrue(coerce_bool(True))
        self.assertTrue(coerce_bool(1))

        self.assertFalse(coerce_bool("False"))
        self.assertFalse(coerce_bool("f"))
        self.assertFalse(coerce_bool("0"))
        self.assertFalse(coerce_bool(""))
        self.assertFalse(coerce_bool(0))
        self.assertFalse(coerce_bool({}))

    @override_settings(NLF_FALSE_VALUES=("a", "b", "c"))
    def test_with_other_settings(self):
        self.assertTrue(coerce_bool("f"))

        self.assertFalse(coerce_bool("aasd"))
        self.assertFalse(coerce_bool("bar"))
        self.assertFalse(coerce_bool("co2"))
