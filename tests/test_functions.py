from .models import Article, Publication
from .utils import BaseTestCase


class DjangoNLFilterFunctionsTestCase(BaseTestCase):
    def test_function_as_value(self):
        filter_expr = "created_at > startOfWeek()"
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertListEqual(list(qs.all()), [self.a4])
