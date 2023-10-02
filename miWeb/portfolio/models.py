from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField('Nombre', max_length=50)
    slug = models.SlugField('Slug', unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
            super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name
            
class Skill(models.Model):
    name = models.CharField('Nombre', max_length=50)
    slug = models.SlugField('Slug', unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
            super(Skill, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField('Titulo', max_length=200)
    description = models.TextField('Descripcion')
    image = models.ImageField(upload_to='projects', null=True, blank=True)
    link = models.URLField('Enlace', max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] 

    def __str__(self):
        return self.title 