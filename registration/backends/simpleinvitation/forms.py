from django import forms
from django.utils.translation import ugettext_lazy as _
from registration.forms import RegistrationFormUniqueEmail
from registration.backends.simpleinvitation.fields import InvitationCodeField

attrs_dict = {'class': 'required'}


class RegistrationFormInvitationCode(RegistrationFormUniqueEmail):
    """Form extending RegistrationFormUniqueEmail.
    Adds two fields - invitation_code and tos for invitation code and TOS
    accept to proceed.

    """
    invitation_code = InvitationCodeField(required=True, max_length=5, label=_(u"Invitation code"))
