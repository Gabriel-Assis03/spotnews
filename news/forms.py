from django import forms
from .validators import validate_title_news, validate_date_format
from .models import News, Category

class CategoryModelsForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Nome'
        # self.fields['name'].widget = forms.TextInput(attrs={
        #         'type': 'text',
        #         'name': 'name',
        #         'maxlength': '200',
        #         'required': 'required'
        #     })

# class NewsModelsForm(forms.ModelForm):
#     class Meta:
#         model = News
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['title'].label = 'Título:'