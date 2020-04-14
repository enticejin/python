from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Category, Banner, Tag, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def hello(request):
    return HttpResponse('hello django')


# Create your views here.
def index1(request):
    # 添加两个变量并赋值
    siteName = "百度一下， 你就知道"
    url = 'www.baidu.com'
    # 新加上一个列表
    list = [
        '开发前的准备',
        '项目需求分析',
        '数据库设计分析',
        '创建项目',
        '基础配置',
        '欢迎页面',
        '创建数据库模型',
    ]
    # 原来的基础上新加字典
    mydict = {
        'name': '吴青峰',
        'qq': '123456',
        'wechart': 'vipMHT',
        'Tel': '10086',
    }
    # 传对象
    allArticles = Article.objects.all()
    # 将两个变量封装
    context = {
        'siteName': siteName,
        'url': url,
        'list': list,  # 把list封装到context
        # 把mydict封装到上下文
        'mydict': mydict,
        # 把查询到的对象装入上下文
        'allArticles': allArticles,
    }
    # 把上下文传递到模板中
    return render(request, 'index1.html', context)


def index_article(request):
    # 对Article进行声明并实例化，然后生成对象allArticles
    allArticles = Article.objects.all()
    # 把查询到的对象装到上下文
    context = {
        'allArticles': allArticles,
    }
    # 把上下文传到模板页面index。html中
    return render(request, 'index_article.html', context)


# 首页
def index(request):
    #查出所有类
    allcategory = Category.objects.all()
    # 查询所有幻灯图数据，并进行切片
    banner = Banner.objects.filter(is_active=True)[0:4]
    # 查询推荐位ID为1的文章
    tui = Article.objects.filter(tui__article__category_id=1)[:3]
    allarticle = Article.objects.all().order_by('-id')[0:10]
    hot = Article.objects.all().order_by('views')[0:10]
    remen = Article.objects.all().filter(tui__article__category_id=2)[0:6]
    link = Link.objects.all()
    tags = Tag.objects.all()
    #把查询出的分类封装到上下文中
    contex = {
        'allcategory': allcategory,
        'banner': banner,
        'tui':tui,
        'allarticle,':allarticle,
        'hot': hot,
        'remen': remen,
        'tags':tags,
        "link": link,
    }
    #传到html页面
    return render(request, 'index.html', contex)


# 列表页
def list(request, lid):
    #获取通过URL传进来的lid，然后筛选出对应文章
    list = Article.objects.filter(category_id=lid)
    # 获取当前文章的栏目名
    cname = Category.objects.get(id=lid)
    # 右侧的热门推荐
    remen = Article.objects.filter(tui__id=2)[0:6]
    # 导航所有分类
    allcategory = Category.objects.all()
    # 右侧所有文章标签
    tags = Tag.objects.all()
    # 在URL中获取当前页面数
    page = request.GET.get('page')
    # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    paginator = Paginator(list, 5)
    try:
        # 获取当前页码的记录
        list = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户输入的页码不是整数时,显示第1页的内容
        list = paginator.page(1)
    except EmptyPage:
        # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
        list = paginator.page(paginator.num_pages)

    return render(request, 'list.html', locals())


# 内容页
def show(request, sid):
    #查询指定id的文章
    show = Article.objects.get(id=sid)
    #导航上的分类
    allcategory = Category.objects.all()
    #右侧所有标签
    tags = Tag.objects.all()
    #右侧热门推荐
    remen = Article.objects.filter(tui__id=2)[:6]
    #内容下面的您可能感兴趣的文章，随机推荐
    Article.objects.all().order_by("?")[:10]
    previous_blog = Article.objects.filter(created_time__gt=show.created_time, category=show.category.id).first()
    netx_blog = Article.objects.filter(created_time__lt=show.created_time, category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'show.html', locals())


# 标签页
def tag(request, tag):
    #通过文章标签进行查询文章
    list = Article.objects.filter(tags__name=tag)
    #热门内容
    remen = Article.objects.filter(tui__id=2)[:6]
    #导航栏内容
    allcategory = Category.objects.all()
    #获取当前内容的标签名
    tname = Tag.objects.get(name=tag)
    #获取分页
    page = request.GET.get('page')
    #所有标签
    tags = Tag.objects.all()
    #分页
    paginator = Paginator(list, 5)
    try:
        # 获取当前页码的记录
        list = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户输入的页码不是整数时,显示第1页的内容
        list = paginator.page(1)
    except EmptyPage:
        # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
        list = paginator.page(paginator.num_pages)
    return render(request, 'tags.html', locals())

# 搜索页
def search(request):
    #获取搜索的关键词
    ss = request.GET.get('search')
    list = Article.objects.filter(title__icontains=ss)  # 获取到搜索关键词通过标题进行匹配
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'search.html', locals())

# 关于我们
def about(request):
    allcategory = Category.objects.all()
    return render(request, 'page.html', locals())
