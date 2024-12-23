from django.db import models

class Post(models.Model):
    #author=models.CharField(max_length=55)
    #image=models.ImageField()
    title=models.CharField(max_length=255)
    content=models.TextField()
    #category=models.IntegerField()
    #tag= models.IntegerField()
    counted_view=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    published_date=models.DateTimeField(null=True)
    created_date= models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
