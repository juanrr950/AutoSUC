from django.utils.deconstruct import deconstructible
from django.core.files.storage import FileSystemStorage
import os


@deconstructible
class CustomFileSystemStorage(FileSystemStorage):

    def get_valid_name(self, name):
        
        return name