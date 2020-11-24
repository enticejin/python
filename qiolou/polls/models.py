import datetime
from django.db import models
from django.utils import timezone
'''
为了在我们的工程中包含这个应用，我们需要在配置类 INSTALLED_APPS 中添加设置。因为 PollsConfig 类写在文件 polls/apps.py 中，
所以它的点式路径是 'polls.apps.PollsConfig'。在文件 qiolou/settings.py 中 INSTALLED_APPS 子项添加点式路径后，
py manage.py makemigrations polls
'''
# Create your models here.每个模型被表示为 django.db.models.Model 类的子类。每个模型有许多类变量，它们都表示模型里的一个数据库字段。
#类 Question
class Question(models.Model):
    #问题最大长度
    question_text = models.CharField(max_length=200)
    #发布时间
    pub_date = models.DateTimeField('date published')
    #输出字符串
    def __str__(self):
        return self.question_text
    #添加一个自定义方法
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#投票选择类
class Choice(models.Model):
    #外键
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #最大长度
    choice_text = models.CharField(max_length=200)
    #默认值0
    votes = models.IntegerField(default=0)
    # 输出字符串
    def __str__(self):
        return self.choice_text