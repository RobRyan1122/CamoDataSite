from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    animal_present = models.BooleanField(default=False)
    animal_type = models.CharField(max_length=100)
    image_file = models.ImageField(upload_to='images/')
    image_title = models.CharField(max_length=100)





class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    animal_present = models.BooleanField(null=True, default=None)
    animal_type = models.CharField(max_length=100)
    clicked_at = models.DateTimeField(auto_now_add=True)
    session_num = models.CharField(max_length=255, default="")
    ap_correct = models.BooleanField(null=True, default=None)
    at_correct = models.BooleanField(null=True, default=None)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='questions', null=True, blank=True)