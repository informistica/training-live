from django.db import models
from django.urls import reverse
 
# Create your models here.
class BlogPostModel(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()
    bozza = models.BooleanField()

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        #return reverse("PostDetailView", kwargs={"pk": self.pk})
        return f"/blog/leggi-post/{self.id}"