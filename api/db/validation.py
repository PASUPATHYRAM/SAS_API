from wtforms import StringField,Form,ValidationError
from wtforms.validators import Length,Email



def custom_email_validator(form,field):
    email=field.data
    if email is None:
        raise ValidationError("Email Required")
    if '@' in email:
        domain=email.split('@')
        domain_check=domain[-1]
        if domain_check.lower() in ['gmail.com','apple.com']:
            return "correct"
        else:
            raise ValidationError("Domain no valid ; try with gmail or apple")
    else:
        raise ValidationError("Invalid email ID")
class UsertableForm(Form):
    phone = StringField('phone', [Length(min=10, max=10)])
    email = StringField('email', [custom_email_validator])

    def __iter__(self):
        fields = super().__iter__()
        return iter([(field.name, field.data) for field in fields])
