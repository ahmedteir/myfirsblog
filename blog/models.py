from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

#allways start the the class name with uppercase letter
#models.Model means that the Post is a Django Model,
#so Django knows that it should be saved in the database.
class Post(models.Model):
    #ForeignKey means relations to another object.
    auther = models.ForeignKey('auth.User')
    #CharField define a text with with limited number.
    title  = models.CharField(max_length=200)
    #TextField - long text without a limit.
    text = models.TextField()
    #DateTimeField - for date and time === the default set timezone.now()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

        def __str__(self):
            return self.title
