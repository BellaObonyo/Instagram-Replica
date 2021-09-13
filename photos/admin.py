from django.contrib import admin
from .models import Follows, Profile, Image,Like,Comment,

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Follows)
admin.site.register(Like)
admin.site.register(Comment)

