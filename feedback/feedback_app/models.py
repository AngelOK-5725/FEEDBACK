from django.db import models

# Create your models here.
class Feedback(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField(max_length=500)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.user_name} - {self.rating}"