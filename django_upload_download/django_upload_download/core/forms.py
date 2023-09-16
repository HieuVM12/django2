from django import forms
from core.models import FileHandler
from django.core.validators import FileExtensionValidator

class FileHandlerForm(forms.ModelForm):

    file_upload = forms.FileField()

    class Meta():
        model = FileHandler
        fields = ('file_upload',)
        file_upload = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['xls', 'xlsx'])]
    )
