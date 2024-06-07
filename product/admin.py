from django.contrib import admin
from .models import productdetails, Myproteindetails,cart
from django.contrib import admin
from .models import productdetails,Comment


admin.site.register(productdetails)
admin.site.register(Myproteindetails)
admin.site.register(cart)
admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)