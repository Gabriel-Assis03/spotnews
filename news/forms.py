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

class NewsModelsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Título'
        self.fields['content'].label = 'Conteúdo'
        self.fields['author'].label = 'Autoria'
        self.fields['created_at'].label = 'Criado em'
        self.fields['created_at'].widget = forms.DateInput(
                attrs={"type": "date"})
        self.fields['image'].label = 'URL da Imagem'
        self.fields['categories'].label = 'Categorias'
