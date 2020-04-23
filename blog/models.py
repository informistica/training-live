from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
 
# Create your models here.
class BlogPostModel(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()
    bozza = models.BooleanField()
    data_creazione = models.DateTimeField(auto_now_add=True)
    autore = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        #return reverse("PostDetailView", kwargs={"pk": self.pk})
        return f"/blog/leggi-post/{self.id}"