from django.utils import timezone

from .factory import nlf_function


@nlf_function("startOfWeek")
def start_of_week(*args, **kwargs):  # pylint: disable=unused-argument
    """
        Determines Monday on the current week. Time is set to `00:00:00`.

        :returns: A datetime object set to 00:00 on Monday of the current week.
        :rtype: :class:`datetime <python:datetime.datetime>`
    """
    now = timezone.now()
    desired_day = now.day - now.weekday()
    return now.replace(day=desired_day, hour=0, minute=0, second=0, microsecond=0)


@nlf_function("startOfMonth")
def start_of_month(*args, **kwargs):  # pylint: disable=unused-argument
    """
        Determines the first day of the current month. Time is set to `00:00:00`.

        :returns: A datetime object set to 00:00 on the first day of the current month.
        :rtype: :class:`datetime <python:datetime.datetime>`
    """
    now = timezone.now()
    return now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)


@nlf_function("startOfYear")
def start_of_year(*args, **kwargs):  # pylint: disable=unused-argument
    """
        Determines the first day of the current year. Time is set to `00:00:00`.

        :returns: A datetime object set to 00:00 on the first day of the current year.
        :rtype: :class:`datetime <python:datetime.datetime>`
    """
    now = timezone.now()
    return now.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
