from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField


class Category(models.Model):
    name = models.CharField('博客分类', max_length=100)
    index = models.IntegerField(default=999, verbose_name='分序排类')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('文章标签', max_length=100)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Recommend(models.Model):
    name = models.CharField('推荐', max_length=100)

    class Meta:
        verbose_name = '推荐'
        verbose_name_plural = verbose_name


class Article(models.Model):
    title = models.CharField('标题', max_length=100)
    excerpt = models.CharField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/',
                            verbose_name='文章图片', blank=True, null=True)
    body = MDTextField(verbose_name='内容')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='作者')
    views = models.PositiveIntegerField('阅读量', default=0)
    recommend = models.ForeignKey(
        Recommend, on_delete=models.DO_NOTHING, verbose_name='推荐', blank=True, null=True)
    create_time = models.DateField('发布时间', auto_now_add=True)
    modify_time = models.DateField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Banner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮播图', upload_to='banner')
    link_url = models.URLField('图片链接', max_length=100)
    is_active = models.BooleanField('是否active', default=False)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text_info


class Link(models.Model):
    name = models.CharField('链接名称', max_length=20)
    link_url = models.URLField('网址', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
