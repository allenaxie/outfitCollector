from django.db import models
from django.urls import reverse

ACCESSORIES_TYPES = (
    ('earring', 'earring'),
    ('necklace', 'necklace'),
    ('bracelet', 'bracelet'),
    ('watch', 'watch'),
    ('hat', 'hat'),
    ('scarf','scarf'),
)


# Create your models here.
class Shoe(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    dress_code = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.color} {self.brand} {self.model}"
    def get_absolute_url(self):
        return reverse('shoes_detail', kwargs={ 'pk': self.id})


class Outfit(models.Model):
    name = models.CharField(max_length=100)
    number_items = models.IntegerField(
        'Number of items in outfit'
    )
    season = models.CharField(max_length=100)
    color_theme = models.CharField(max_length=100)
    dress_code = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    def __str__ (self):
        return self.name
    def get_absolute_url(self):
        return reverse('outfits_detail', kwargs={ 'outfit_id': self.id})
    shoes = models.ManyToManyField(Shoe)


class Accessories(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=100,
        choices= ACCESSORIES_TYPES,
        default = ACCESSORIES_TYPES[0][0],
    )
    date= models.DateField(
        'Add accessory date'
    )
    dress_code = models.CharField(max_length=100)
    # CASCADE ensures all accessories under the outfit we delete are also deleted
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()} on {self.date}"

    class Meta:
        ordering = ['-date']



    