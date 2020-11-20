from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock, patch

from django_nlf.functions import FunctionFactory


MIDWEEK = Mock()
MIDWEEK.now.return_value = datetime(2020, 11, 18, 13, 26, 43, 1234)

STARTOFWEEK = Mock()
STARTOFWEEK.now.return_value = datetime(2020, 11, 16, 13, 26, 43, 1234)


@patch("django_nlf.functions.dates.timezone", MIDWEEK)
class DateFunctionsMidweekTestCase(TestCase):
    def test_start_of_year(self):
        start_of_year = FunctionFactory.get_function("startOfYear")
        self.assertEqual(start_of_year(), datetime(2020, 1, 1))

    def test_start_of_month(self):
        start_of_month = FunctionFactory.get_function("startOfMonth")
        self.assertEqual(start_of_month(), datetime(2020, 11, 1))

    def test_start_of_week_midweek(self):
        start_of_week = FunctionFactory.get_function("startOfWeek")
        self.assertEqual(start_of_week(), datetime(2020, 11, 16))


@patch("django_nlf.functions.dates.timezone", STARTOFWEEK)
class DateFunctionsStartOfWeekTestCase(TestCase):
    def test_start_of_week_start(self):
        start_of_week = FunctionFactory.get_function("startOfWeek")
        self.assertEqual(start_of_week(), datetime(2020, 11, 16))
