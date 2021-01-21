from django.utils.deconstruct import deconstructible
from django.core.files.storage import FileSystemStorage
import os
from AutoSUC import settings


@deconstructible
class CustomFileSystemStorage(FileSystemStorage):
    
    def get_available_name(self, name, max_length=None):
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name
    
    def get_valid_name(self, name):
        
        return name