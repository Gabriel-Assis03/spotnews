# from django import forms
# from .validators import validate_title_news, validate_date_format
# from .models import News

# class NewsModelsForm(forms.ModelForm):
#     class Meta:
#         model = News
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['title'].validate = [validate_title_news]
#         self.fields['created_at'].validate = [validate_date_format]