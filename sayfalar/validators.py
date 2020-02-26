from django.core.exceptions import ValidationError

def tc_validate(value):
    if len(value)<11 and value>1:
        raise ValidationError('T.C. No. 11 rakamdan az olamaz. ')
    return value