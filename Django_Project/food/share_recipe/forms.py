from django import forms
from .models import share_recipe, Answer, Comment

class RecipeForm(forms.ModelForm):
    class Meta:
        model = share_recipe
        fields = ['subject', 'menu', 'material', 'how_Make']
        labels = {
            'subject' : '레시피 이름',
            'menu' : '종류',
            'material' : '재료',
            'how_Make' : '만드는 법',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변 내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : '댓글내용'
        }