from django.db import models
from django.contrib.auth.models import User

class Label(models.Model):
    name = models.CharField(max_length=300)
    def __str__ (self):
        return self.name

class Thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    label = models.ForeignKey(Label, on_delete=models.SET_NULL, null = True)
    topic = models.CharField(max_length = 300)
    description = models.TextField(null = False, blank = False)
    #participants
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__ (self):
        return self.topic
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return self.body[0:50]
    
    