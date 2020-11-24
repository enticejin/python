from django.contrib import admin
from.models import Question
# Register your models here.
#注册后台管理账户添加Question
admin.site.register(Question)
