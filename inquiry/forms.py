from django import forms
from django.forms import DateInput

from inquiry.models import Otp, Inquiry


class MobileVerificationForm(forms.ModelForm):

    class Meta:
        model = Otp
        fields = ['mobile_number']
        widgets = {
            'mobile_number': forms.TextInput(
                attrs={
                    'class': 'input-group form-control phone',
                    'pattern': '[0-9]+',
                    'title': 'Only numbers allowed',
                    'type': "tel",
                    'placeholder': "Mobile Number"
                }
            ),
        }


class OtpForm(forms.ModelForm):

    class Meta:
        model = Otp
        fields = ['otp']
        widgets = {
            'otp': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg form-control-alt',
                    'pattern': '[0-9]+',
                    'title': 'Only numbers allowed',
                    'placeholder': "Enter OTP"
                }
            ),
        }


class InquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'start_date', 'end_date', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input-group form-control',
                'title': 'Numbers and special characters are not allowed.',
                'placeholder': 'Full Name'
            }),
            'email': forms.TextInput(attrs={
                'class': 'input-group form-control',
                # 'title': 'Numbers and special characters are not allowed.'
                'placeholder': 'Email'
            }),
            # 'start_date': forms.DateTimeInput(attrs={
            #     'type': "text",
            #     'name': "example-datepicker1",
            #     'class': 'js-datepicker form-control js-datepicker-enabled',
            #     'id': "example-datepicker1",
            #     'data-week-start': "1",
            #     'data-autoclose': "true",
            #     'data-today-highlight': "true",
            #     'data-date-format': "mm/dd/yy",
            #     'placeholder': "mm/dd/yy"
            # }),
            'start_date': forms.SelectDateWidget(years=range(1990, 2022)),
            'end_date': forms.SelectDateWidget(years=range(1990, 2022)),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter your complaint here.'
            }),
        }