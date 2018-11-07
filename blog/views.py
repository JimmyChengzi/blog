import logging
from django.shortcuts import render
from django.conf import settings
from blog.models import *
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger

logger = logging.getLogger('blog.views')

#在setting下template中设置上下文处理
def global_setting(request):
    return {
        'SITE_NAME':settings.SITE_NAME,
        'SITE_DESC':settings.SITE_DESC,
    }

def index(request):
    try:
        # 分类信息获取(导航)
        category_list = Category.objects.all()[:5]
    except Exception as e:
        logger.error(e)
    #广告数据
    ad_list = Ad.objects.all()
    #最新文章数据
    article_list = Article.objects.all()
    #创建一个分页对象,默认10条数据
    paginator = Paginator(article_list,2)
    #检查分页,捕获分页异常
    try:
        page = int(request.GET.get('page',1))
        article_list = paginator.page(page)
    except (InvalidPage,EmptyPage,PageNotAnInteger): #三种分页异常
        article_list = paginator.page(1)
    return render(request, 'index.html', locals())