from django.contrib import admin
from blogapp.models import Blog,Contact

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    class Media:
        css ={
            "all":("main.css",)
        }

        js=("blog.js",)


        
admin.site.register(Blog,BlogAdmin) #register BLOG model to admin 
admin.site.register(Contact)        #register Contact model to admin 



