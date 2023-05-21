from django.contrib import admin

# Register your models here.

#from .models import Question

#telling that the Question ovjects have an admin interface 
#admin.site.register(Question)

from .models import Thread, Message, Label

admin.site.register(Thread)
admin.site.register(Message)
admin.site.register(Label)