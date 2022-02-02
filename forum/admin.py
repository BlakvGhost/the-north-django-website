from django.contrib import admin
from .models import ForumModel,PubTags,Category

# Register your models here.
admin.site.register(ForumModel)
admin.site.register(PubTags)
admin.site.register(Category)