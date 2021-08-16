from django.db import models
# Create your models here.

class Location(models.Model):
    name= models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Participants(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField(unique=True)

    def __str__(self):
        return f'{self.email}'


class Meetme(models.Model):
    title = models.CharField(max_length=200)    
    slug = models.SlugField(unique=True)
    description = models.TextField()

    image = models.ImageField(upload_to='images')
    organizer_email = models.EmailField()
    date = models.DateField()

    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participants, blank=True, null=True)

    def __str__(self):
        return f'{self.title}-{self.slug}'
