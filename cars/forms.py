from django import forms
from .models import Review
from django.forms import ModelForm


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'surname', 'rating']

        labels = {
            'first_name': "Your First Name",
            'surname': "Your Surname",
            'rating': "Your Rating"
        }

        error_messages = {
            'rating': {
                'min_value': "YO! Min value is 1",
                'max_value': "YO! Min value is 5"
            }
        }
