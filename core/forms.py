from django import forms

from .models import ContactEnquiry, MembershipApplication


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactEnquiry
        fields = ["name", "phone", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Full name"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "+256 700 000 000"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "name@example.com"}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Membership or service enquiry"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Tell us how we can help you"}),
        }
        labels = {
            "name": "Full name",
            "phone": "Phone number",
            "email": "Email address",
            "subject": "Subject",
            "message": "Message",
        }


class MembershipApplicationForm(forms.ModelForm):
    class Meta:
        model = MembershipApplication
        fields = [
            "full_name",
            "gender",
            "phone",
            "email",
            "district",
            "sub_county",
            "village",
            "occupation",
            "farmer_type",
            "preferred_contact",
            "message",
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your full name"}),
            "gender": forms.Select(attrs={"class": "form-select"}, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")]),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "+256 700 000 000"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "name@example.com"}),
            "district": forms.TextInput(attrs={"class": "form-control", "placeholder": "District"}),
            "sub_county": forms.TextInput(attrs={"class": "form-control", "placeholder": "Sub-county"}),
            "village": forms.TextInput(attrs={"class": "form-control", "placeholder": "Village"}),
            "occupation": forms.TextInput(attrs={"class": "form-control", "placeholder": "Occupation"}),
            "farmer_type": forms.TextInput(attrs={"class": "form-control", "placeholder": "Farmer or Trader"}),
            "preferred_contact": forms.Select(attrs={"class": "form-select"}, choices=[("Phone", "Phone"), ("WhatsApp", "WhatsApp"), ("Email", "Email")]),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Tell us how we can support you"}),
        }
        labels = {
            "full_name": "Full name",
            "gender": "Gender",
            "phone": "Phone number",
            "email": "Email address",
            "district": "District",
            "sub_county": "Sub-county",
            "village": "Village",
            "occupation": "Occupation",
            "farmer_type": "Type of farmer/trader",
            "preferred_contact": "Preferred contact method",
            "message": "Message",
        }
