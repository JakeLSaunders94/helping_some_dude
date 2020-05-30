from django.db import models

'''
Step 1 - Create a model called genres, this only has the genre name
but you will no doubt need to add some more fields / properties at some point
and this means you'll be able to query the data properly without a bunch of weird 
text querys, which are slow and messy.
'''


class Genre(models.Model):
    # Note, charfields and textfields are the same but for one liners charfields are rendered better in forms.
    Genre_Name = models.CharField(max_length=250,  # Required for char fields
                                  verbose_name="Genre of Game")  # Renders the form label better


class Console_Platform(models.Model):
    # Same sort of thing here, but i've added more stuff (see below)
    Platform_Name = models.CharField(max_length=250,  # Required for char fields
                                     verbose_name="Genre of Game")  # Renders the form label better
    Release_Date = models.DateField(verbose_name="Console Release Date")
    # So now you have release date as part of the platform model
    # See my query example below for why this is good.


# Feel free to follow this proforma for game rating, or whatever else you like.

class Game(models.Model):
    Game_Name = models.CharField(max_length=250,
                                 verbose_name="Game Name")
    #  Note, this could be many to many, but I've done a 1 to 1 just for demo purposes.
    Genre = models.ForeignKey(Genre,  # Linked model# )
                              on_delete=models.CASCADE,  # This is required for ForeignKeys, google it.
                              verbose_name="Genre")
    Released_On_Consoles = models.ManyToManyField(Console_Platform)  # Linked model


