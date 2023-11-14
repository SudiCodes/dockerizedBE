from django import forms
from .models import File, ImageFile


class FileModelForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file',)


class ImageModelForm(forms.ModelForm):
    class Meta:
        model = ImageFile
        fields = ('img_file',)
