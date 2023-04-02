from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
class Tool(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
class Project(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to="myportfolio/files/covers")
    sourcelink = models.CharField(max_length=200, blank=True, null=True)
    livelink = models.CharField(max_length=200, blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    tools = models.ManyToManyField(Tool)
    rank = models.IntegerField()
    CATEGORY_CHOICES = [
        ('none', 'None'),
        ('mobile', 'Mobile'),
        ('web', 'WEB'),
    ]
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default='None',
    )
    
    def __str__(self) -> str:
        return f"{self.rank}: {self.name} ({self.category})"