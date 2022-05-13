from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):
    class Meta: #약속! ModelForm에서의 조건
        model = GuessNumbers
        fields=('name','text',) #유저에게 입력받을 열
