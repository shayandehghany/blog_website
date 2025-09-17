from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','status','datetime_created')
    list_filter = ('datetime_created',)



# admin.site.register(Post)

# Register your models here.
