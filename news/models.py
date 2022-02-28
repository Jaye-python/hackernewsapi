from django.db import models
from django.urls import reverse

# Create your models here.

class News(models.Model):
    
    hacker_id = models.IntegerField(default=1, primary_key=True, db_index=True)
    type = models.CharField ( max_length=100, default='None', null=True)
    creator = models.CharField ( max_length=100, default='None', null=True)
    descendants = models.IntegerField(default=1, blank=True, null=True)
    score = models.IntegerField(default=1, null=True)
    title = models.CharField ( max_length=100, default='None', null=True)
    url = models.CharField ( max_length=500, default='None', null=True)
    api_created = models.BooleanField(default=False) # This field is used to identify db objects created via API and only items with this field set to True will be permitted to be deleted
    
    
    class Meta:
        db_table = 'news'
        ordering = ['-hacker_id', ]
        get_latest_by = ['-hacker_id' ]
    

    def __str__(self):
        return str(self.hacker_id)
    

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk' : self.pk})