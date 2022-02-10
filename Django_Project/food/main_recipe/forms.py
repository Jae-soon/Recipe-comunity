from django import forms
from .models import main_recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = main_recipe
        fields = ['subject', 'menu', 'material', 'how_Make']
        labels = {
            'subject' : '레시피 이름',
            'menu' : '종류',
            'material' : '재료',
            'how_Make' : '만드는 법',
        }