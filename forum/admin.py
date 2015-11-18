from django.contrib import admin
from forum.models import topic, post, node, classify
# Register your models here.

admin.site.register(topic)
admin.site.register(post)
admin.site.register(node)
admin.site.register(classify)
