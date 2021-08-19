"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
#导入静态模块文件
from django.conf import settings
#导入配置文件里的文件上传配置
from blog import views

urlpatterns = [
    #管理后台
    path('admin/', admin.site.urls),
    #文章首页
    path('', views.index, name='index'),
    #未修改前的首页
    path('index1/', views.index1),
    #修改后的首页
    #path('index/', views.index, name="index"),
    #列表页
    path('list-<int:lid>.html', views.list, name='list'),
    #内容页
    path('show-<int:sid>.html', views.show, name='show'),
    #标签列表页
    path('tag/<tag>', views.tag, name='tags'),
    #搜索列表页
    path('s/', views.search, name='search'),
    #联系我们单页
    path('about/', views.about, name='about'),
    path('ueditor/', include('DjangoUeditor.urls')), #添加DjangoUeditor的URL
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}), #增加此行
]
