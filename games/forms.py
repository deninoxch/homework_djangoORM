from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'release_date', 'is_free', 'developer', 'genres']