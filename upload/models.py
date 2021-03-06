# System libraries
from datetime import date
from django.db import models

# Application-wide settings
from dnollkse import settings

"""
uploads.models module.

In this moduel we define the model for our uploaded files.
The only special things here are the functions used to ensure that the files are
saved in a easy-to-access location.
"""

def setFilePath(instance, filename):
    """
    Creates the base directory where we save the image.
    It is saved in STATIC_ROOT/uploads/YYYY/
    """
    year = date.today().year
    ext = instance.name.split('.')[-1]

    return '/'.join([str(year), filename])

class Upload(models.Model):
    """
    Upload model.

    Represents an uploaded image with a name, image field and alt text.
    The image is stored on disk as /uploads/YYYY/name.ext.
    """
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=setFilePath)
    alt = models.TextField(blank=True)
    date_uploaded = models.DateField(default=date.today)

    def __str__(self):
        """
        Overrides the default __str__ (ToString equivalent in other languages)
        with a function that returns the name of the upload.
        """
        return self.name

    def save(self, *args, **kwargs):
        """
        Overrides the save function to save the file where we want.
        It is saved with the name of the upload as the image filename.
        """
        fileName = self.photo.name.split('/')[-1]
        ext = fileName.split('.')[-1]
        self.photo.name = self.name + '.' + ext
        super(Upload, self).save(*args, **kwargs)

    def render(self, **kwargs):
        """
        Returns an HTML img element with the uploaded image.
        Accepts positional arguments id, cls and style for setting the id,
        class and style of the rendered upload.
        """
        iId = kwargs.get('id')
        iClass = kwargs.get('cls')
        iStyle = kwargs.get('style')
        elemId = ''
        elemClass = ''
        elemStyle = ''

        if iId != None:
            elemId = 'id="' + iId + '"'

        if iClass != None:
            elemClass = 'class="' + iClass + '"'

        if iStyle != None:
            elemStyle = 'style="' + iStyle + '"'

        return '<img src="' + self.photo.url + '" alt="' + self.alt +'" ' + elemId + ' ' + elemClass + elemStyle + '/>'

    @staticmethod
    def route(uploadName):
        """
        Takes a string matching the name of an upload and
        returns the path to that upload's image.

        Might be used in routing in a relatively close feature.
        """
        u = Upload.objects.get(name=uploadName)
        return u.photo.name

# Receive the pre_delete signal and delete the file
# associated with the model instance.
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver

@receiver(post_delete, sender=Upload)
def upload_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.photo != None:
        instance.photo.delete(False)
