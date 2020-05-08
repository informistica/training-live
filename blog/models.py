from django.db import models
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.models import User
 
# Create your models here.
class BlogPostModel(models.Model):
    titolo = models.CharField(max_length=50)
    contenuto = models.TextField()
    autore = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    bozza = models.BooleanField()
    data_creazione = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titolo

    #def get_absolute_url(self):
        #return reverse("PostDetailView", kwargs={"pk": self.pk})
        # return redirect("leggi-post", kwargs={"pk": self.pk})
    #   return f"/blog/leggi-post/{self.id}"
   

class BlogCommentModel(models.Model):
    post = models.ForeignKey(BlogPostModel,
                             on_delete=models.CASCADE,
                             related_name='comments')
    autore = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    contenuto = models.TextField()
    data_creazione = models.DateTimeField(auto_now_add=True)
    attivo = models.BooleanField(default=True)
    punti = models.SmallIntegerField(default=1)

    class Meta:
        ordering = ('data_creazione',)

    def __str__(self):
        return f'Commento di {self.autore} su {self.post}'