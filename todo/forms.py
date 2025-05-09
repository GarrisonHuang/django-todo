from .models import Todo
from django.forms import ModelForm


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "text", "date_completed", "important", "completed"]
        # fields = "__all__"
