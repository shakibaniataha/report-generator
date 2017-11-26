from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_comma_separated(string):
    try:
        string.split(',')

    except:
        raise ValidationError(
            _('The input must be a string of comma-separated fields'),
        )