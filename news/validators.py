from django.core.exceptions import ValidationError
from datetime import datetime


def validate_title_news(value):
    if len(value.split()) <= 1:
        raise ValidationError(
            "O título deve conter pelo menos 2 palavras."
        )
    

def validate_date_format(value):
    try:
        datetime.strptime(str(value), "%Y-%m-%d")
    except ValidationError:
        raise ValidationError("O formato da data deve ser AAAA-MM-DD.")