from django.forms import ModelForm, fields
from screener.models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['slug']