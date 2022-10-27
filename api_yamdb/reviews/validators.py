from datetime import datetime

from rest_framework.exceptions import ValidationError


def year_validator(value):
    if value < 0 or value > datetime.now().year:
        raise ValidationError('Вы ввели неверный год')
