from django.db import models

# Create your models here.
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

class Profile(models.Model):
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    name = models.CharField('Nombre', max_length=50)
    bio = models.CharField('bio', max_length=50)
    about = models.TextField('Acerca de mi', null=True, blank=True)
    cv = models.FileField('CV', upload_to='cvs', max_length=100, null=True, blank=True)
    email = models.EmailField('Correo electronico', max_length=254, null=True, blank=True)

    class Meta:
        verbose_name = 'Mi perfil'

    def __str__(self):
        return f'Mi perfil: {self.name}'





    


