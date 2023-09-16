from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator
import os
from django.contrib.auth import get_user_model
User = get_user_model()
def file_path(instance,filename):
    path = "documents/"
    format = '' + filename
    return os.path.join(path,format) 

# Create your models here.
class FileHandler(models.Model):
    file_upload = models.FileField(upload_to=file_path,validators=[FileExtensionValidator(allowed_extensions=['xls', 'xlsx'])])
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
        verbose_name="posted by", on_delete=models.SET_NULL)
    def __str__(self):
        return os.path.basename(self.file_upload.name) +" - Người đăng: "+ str(self.posted_by)

    
