from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('Game_Name', 'Genre', 'Released_On_Consoles')

    '''
    Rendering the form like this will automatically give you the multiple select and
    single select forms you need.
    Some side points: 
    1. When you save the form as a new model, do not use blabla.save(commit=False)
        followed by blabla.save(), manytomany saves require a straight save
    2. If you're just starting out, take a look at django-crispy-forms, it makes forms not look horrible and
    is dead easy to use.
    '''