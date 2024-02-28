from django.db import models
from django.core.validators import MinValueValidator

from my_music_app.profiles.models import Profile


# class Genre(models.TextChoices):
#     GENRE_POP = "Pop Music"
#     GENRE_JAZZ = "Jazz Music"
#     GENRE_ROCK = "Rock Music"
#     GENRE_COUNTRY = "Country Music"
#     GENRE_RNB = "R&B Music"
#     GENRE_DANCE = "Dance Music"
#     GENRE_HIP_HOP = "Hip Hop Music"
#     GENRE_OTHER = "Other"

class Album(models.Model):
    MIN_LENGTH_NAME = 30
    MIN_LENGTH_ARTIST_NAME = 30
    MIN_LENGTH_GENRE = 30
    MIN_VALUE_PRICE = 0.0
    
    class Genres(models.TextChoices):
        POP_MUSIC = "Pop Music", "Pop Music"
        JAZZ_MUSIC = "Jazz Music", "Jazz Music"
        R_AND_B_MUSIC = "R&B Music", "R&B Music"
        ROCK_MUSIC = "Rock Music", "Rock Music"
        COUNTRY_MUSIC = "Country Music", "Country Music"
        DANCE_MUSIC = "Dance Music", "Dance Music"
        HIP_HOP_MUSIC = "Hip Hop Music", "Hip Hop Music"
        OTHER = "Other", "Other"

    name = models.CharField(
        max_length=MIN_LENGTH_NAME,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Album Name',
    )

    artist_name = models.CharField(
        max_length=MIN_LENGTH_ARTIST_NAME,
        blank=False,
        null=False,
        verbose_name='Artist'
    )

    genre = models.CharField(
        max_length=30,
        choices=Genres,
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_VALUE_PRICE),
        ),
        blank=False,
        null=False,
    )
    
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
