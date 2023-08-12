from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Marks(models.Model):
    Student = models.CharField(max_length = 20)
    Class = models.CharField(max_length = 20)
    Admission = models.IntegerField()
    EnglishScore = models.IntegerField()
    MathsScore = models.IntegerField()
    ScienceScore = models.IntegerField()
    KiswahiliScore = models.IntegerField()
    SSCREScore = models.IntegerField()
    TotalScore = models.IntegerField()

    def __unicode__(self):
        return "%s plus %s plus %s plus %s plus %s is %s " % (self.EnglishScore, self.MathsScore, self.ScienceScore, self.KiswahiliScore, self.SSCREScore, self.EnglishScore + self.MathsScore + self.ScienceScore + self.KiswahiliScore + self.SSCREScore)

class Portal(models.Model):
    # user = models.OneToOneField(User, on_delete = models.CASCADE) #Delete profile when user is deleted
    img = models.ImageField(default = 'default.png', upload_to = 'images/')
    desc = models.TextField()

def __str__(self):
   return f'{self.user.username} Portal'

