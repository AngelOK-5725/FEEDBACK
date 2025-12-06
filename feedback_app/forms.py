from django import forms
from .models import Feedback

# class review_form(forms.Form):
#     user_name = forms.CharField(label='Your Name:', max_length=100, error_messages=
#         {'required': 'Please enter your name.',
#         'max_length': 'Name cannot exceed 100 characters.'})
#     review_text = forms.CharField(label='Your Feedback:', widget=forms.Textarea, max_length=500)
#     rating = forms.IntegerField(label='Rating (1-5):', min_value=1, max_value=5)

class review_form(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        # Alternatively, you can specify fields explicitly:
        # fields = ['user_name', 'review_text', 'rating']
        labels = {
            'user_name': 'Your Name:',
            'review_text': 'Your Feedback:',
            'rating': 'Rating (1-5):'
        }
        error_messages = {
            'user_name': {
                'required': 'Please enter your name.',
                'max_length': 'Name cannot exceed 100 characters.'
            },
            'review_text': {
                'required': 'Please enter your feedback.',
                'max_length': 'Feedback cannot exceed 500 characters.'
            },
            'rating': {
                'required': 'Please provide a rating between 1 and 5.',
                'min_value': 'Rating must be at least 1.',
                'max_value': 'Rating cannot exceed 5.'
            }
        }