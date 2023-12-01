from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)


class HashTag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Equipment(models.Model):
    image = models.ImageField(upload_to='images', null=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.FloatField(default=0)
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hashtags = models.ManyToManyField(
        'post.HashTag',
        blank=True,
        related_name='posts'
    )
    categories = models.ManyToManyField(
        'Category',
        blank=True,
        related_name='posts'
    )

    def __str__(self) -> str:
        return f'{self.id} {self.title}'

class Review(models.Model):
    post = models.ForeignKey('post.Equipment',
                             on_delete=models.CASCADE,
                             related_name='reviews'
                             )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# post = Equipment.objects.get(id=1)
# post.reviews.all()  #QuerySet
#
# review = Review.objects.get(id=1)
# review.post  # 1 obj

class Feedback(models.Model):
    title = models.TextField()
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)




