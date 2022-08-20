from django.contrib import admin

from .models  import User,Room,Cilent,Amenities,Image

# Register your models here.

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Cilent)
admin.site.register(Image)
admin.site.register(Amenities)