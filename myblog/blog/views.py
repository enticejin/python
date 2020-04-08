from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def hello(request):
    return HttpResponse('hello django')
# Create your views here.
def index(request):
    #添加两个变量并赋值
    siteName= "百度一下， 你就知道"
    url = 'www.baidu.com'
    #新加上一个列表
    list =[
        '开发前的准备',
        '项目需求分析',
        '数据库设计分析',
        '创建项目',
        '基础配置',
        '欢迎页面',
        '创建数据库模型',
    ]
    #原来的基础上新加字典
    mydict = {
        'name':'吴青峰',
        'qq':'123456',
        'wechart':'vipMHT',
        'Tel':'10086',
    }
    #传对象
    allArticles = Article.objects.all()
    #将两个变量封装
    context = {
        'siteName':siteName,
        'url':url,
        'list':list,#把list封装到context
        #把mydict封装到上下文
        'mydict':mydict,
        #把查询到的对象装入上下文
        'allArticles':allArticles,
    }
    #把上下文传递到模板中
    return render(request, 'index.html', context)

def index_article(request):
    #对Article进行声明并实例化，然后生成对象allArticles
    allArticles = Article.objects.all()
    #把查询到的对象装到上下文
    context = {
        'allArticles': allArticles,
    }
    #把上下文传到模板页面index。html中
    return render(request, 'index_article.html', context)

    