from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    objects = None
    REALISM_IMPRESSIONISM = None
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    image = models.ImageField()

    THEME1 = 'theme1' # impressionism = pastel color interior
    THEME2 = 'theme2' # realism = palace
    THEME3 = 'theme3' # orientalism + animation = warm color interior
    THEME4 = 'theme4' # abstract + pop_art = primary color interior
    THEME5 = 'theme5' # pencil_drawing = white/black interior

    PREDICTION_CHOICES = [
        (THEME1, 'theme1'),
        (THEME2, 'theme2'),
        (THEME3, 'theme3'),
        (THEME4, 'theme4'),
        (THEME5, 'theme5'),
    ]
    prediction = models.CharField(choices=PREDICTION_CHOICES, max_length=22)

    public = models.BooleanField(default=True)
