from django.test import TestCase
from .models import Developer, Game

class GameModelTest(TestCase):
    def test_str_returns_title(self):
        dev = Developer.objects.create(
            company_name="Test Studio",
            country="USA",
            language="Python"
        )
        game = Game.objects.create(
            title="Test Game",
            description="desc",
            release_date="2020-01-01",
            is_free=True,
            developer=dev
        )
        self.assertEqual(str(game), "Test Game")