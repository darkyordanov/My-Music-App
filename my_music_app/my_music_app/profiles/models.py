from django.core.validators import MinLengthValidator
from django.db import models

from my_music_app.profiles.validators import valid_username


class Profile(models.Model):
    MAX_LENGTH_USERNAME = 15
    MIN_LENGTH_USERNAME = 2
    
    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=(
            MinLengthValidator(MIN_LENGTH_USERNAME),
            valid_username,
        ),
        blank=False,
        null=False,
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.username