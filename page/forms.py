from django.forms import ModelForm
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        labels = {
            "name" : "Imię",
            "company" : "Nazwa Firmy",
            "opinion" : "Twoja opinia",
        }