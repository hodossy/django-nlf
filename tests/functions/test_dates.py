from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock, patch

from django_nlf.functions import FunctionFactory


MID_WEEK = Mock()
MID_WEEK.now.return_value = datetime(2020, 11, 18, 13, 26, 43, 1234)

START_OF_WEEK = Mock()
START_OF_WEEK.now.return_value = datetime(2020, 11, 16, 13, 26, 43, 1234)

MID_WEEK_ANOTHER_MONTH = Mock()
MID_WEEK_ANOTHER_MONTH.now.return_value = datetime(2020, 12, 4, 13, 26, 43, 1234)

MID_WEEK_ANOTHER_YEAR = Mock()
MID_WEEK_ANOTHER_YEAR.now.return_value = datetime(2021, 1, 2, 13, 26, 43, 1234)



class DateFunctionsMidweekTestCase(TestCase):
    @patch("django_nlf.functions.dates.timezone", MID_WEEK)
    def test_start_of_year(self):
        start_of_year = FunctionFactory.get_function("startOfYear")
        self.assertEqual(start_of_year(), datetime(2020, 1, 1))

    @patch("django_nlf.functions.dates.timezone", MID_WEEK)
    def test_start_of_month(self):
        start_of_month = FunctionFactory.get_function("startOfMonth")
        self.assertEqual(start_of_month(), datetime(2020, 11, 1))

    @patch("django_nlf.functions.dates.timezone", MID_WEEK)
    def test_start_of_week_midweek(self):
        start_of_week = FunctionFactory.get_function("startOfWeek")
        self.assertEqual(start_of_week(), datetime(2020, 11, 15))
        with patch("django_nlf.functions.dates.FIRST_DAY_OF_WEEK", 0):
            self.assertEqual(start_of_week(), datetime(2020, 11, 16))
        with patch("django_nlf.functions.dates.FIRST_DAY_OF_WEEK", 5):
            self.assertEqual(start_of_week(), datetime(2020, 11, 14))


    @patch("django_nlf.functions.dates.timezone", MID_WEEK_ANOTHER_MONTH)
    def test_start_of_week_in_previous_month_midweek(self):
        start_of_week = FunctionFactory.get_function("startOfWeek")
        self.assertEqual(start_of_week(), datetime(2020, 11, 29))
        with patch("django_nlf.functions.dates.FIRST_DAY_OF_WEEK", 0):
            self.assertEqual(start_of_week(), datetime(2020, 11, 30))
        with patch("django_nlf.functions.dates.FIRST_DAY_OF_WEEK", 5):
            self.assertEqual(start_of_week(), datetime(2020, 11, 28))

    @patch("django_nlf.functions.dates.timezone", MID_WEEK_ANOTHER_YEAR)
    def test_start_of_week_in_previous_year_midweek(self):
        start_of_week = FunctionFactory.get_function("startOfWeek")
        self.assertEqual(start_of_week(), datetime(2020, 12, 27))
        with patch("django_nlf.functions.dates.FIRST_DAY_OF_WEEK", 0):
            self.assertEqual(start_of_week(), datetime(2020, 12, 28))
        with patch("django_nlf.functions.dates.FIRST_DAY_OF_WEEK", 5):
            self.assertEqual(start_of_week(), datetime(2020, 12, 26))

    @patch("django_nlf.functions.dates.timezone", START_OF_WEEK)
    def test_start_of_week_start(self):
        start_of_week = FunctionFactory.get_function("startOfWeek")
        self.assertEqual(start_of_week(), datetime(2020, 11, 15))
        with patch("django_nlf.functions.dates.FIRST_DAY_OF_WEEK", 0):
            self.assertEqual(start_of_week(), datetime(2020, 11, 16))
        with patch("django_nlf.functions.dates.FIRST_DAY_OF_WEEK", 5):
            self.assertEqual(start_of_week(), datetime(2020, 11, 14))
