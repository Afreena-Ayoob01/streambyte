from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Movie, Comment

class RegistrationForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=100,
        required=True
    )

    last_name = forms.CharField(
        max_length=100,
        required=True
    )

    email = forms.EmailField(
        required=True
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'This email is already registered.'
            )

        return email

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = [
            'title',
            'poster',
            'description',
            'release_date',
            'actors',
            'rating',
            'category',
            'trailer_link',
        ]

        widgets = {
            'release_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'text',
        ]

        widgets = {
            'text': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': 'Write your comment...'
                }
            ),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'Write your review...',
                    'rows': 5
                }
            )
        }
