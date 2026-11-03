from django import forms
from django.utils import timezone

from .models import Appointment,Contact


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "customer_name",
            "customer_email",
            "customer_phone",
            "service",
            "appointment_at",
            "notes",
        ]
        widgets = {
            "customer_name": forms.TextInput(attrs={"class": "form-control", "autocomplete": "name"}),
            "customer_email": forms.EmailInput(attrs={"class": "form-control", "autocomplete": "email"}),
            "customer_phone": forms.TelInput(attrs={"class": "form-control", "autocomplete": "tel"}),
            "service": forms.Select(attrs={"class": "form-select"}),
            "appointment_at": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }
        labels = {
            "customer_name": "Full name",
            "customer_email": "Email address",
            "customer_phone": "Phone number",
            "service": "Choose a service",
            "appointment_at": "Preferred date and time",
            "notes": "Additional notes",
        }
        help_texts = {
            "appointment_at": "Your appointment is pending until the studio confirms it.",
        }

    def clean_appointment_at(self):
        appointment_at = self.cleaned_data["appointment_at"]
        if appointment_at <= timezone.now():
            raise forms.ValidationError("Choose a date and time in the future.")
        return appointment_at
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact

        fields = [
            "contact_name",
            "contact_surname",
            "contact_email",
            "contact_comment",
        ]

        widgets = {
            "contact_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your first name"
            }),

            "contact_surname": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your last name"
            }),

            "contact_email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Your email address"
            }),

            "contact_comment": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Write your message here..."
            }),
        }

        labels = {
            "contact_name": "First Name",
            "contact_surname": "Last Name",
            "contact_email": "Email Address",
            "contact_comment": "Your Message",
        }