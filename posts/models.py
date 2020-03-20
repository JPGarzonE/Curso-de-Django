"""Posts models."""

# Django
from django.db import models
from users.models import User

class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
        # la idea es que el on_delete este protegido ya que generalmente 
        # no queremos que se borren los datos por lo valiosos que son para el negocio
    )

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return '{} by @ {}'.format(self.title, self.user.username)