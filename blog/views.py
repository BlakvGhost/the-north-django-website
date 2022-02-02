from django.shortcuts import render
from dashbord.models import Pblog
from forum.views import sidebar,pagine

# Create your views here.
def blog(response):
    all = Pblog.objects.all().order_by('-id')
    page = pagine(all,10,response.GET.get('p'))
    sidebarF = sidebar(Pblog,"Blog")
    context = {'all': page.get('post'),'posts': sidebarF.get('postBar'),'stags': sidebarF.get('stags'),
               'category':sidebarF.get(
        'category'),'section':sidebarF.get('section'), 'page': page.get('totalPage'),}
    return render(response,'blog/blog.html',context)

def detail(response,pk):
    all = Pblog.objects.get(id=pk)
    sidebarF = sidebar(Pblog, "Blog")
    context = {'posts': sidebarF.get('postBar'), 'stags': sidebarF.get('stags'),
               'category': sidebarF.get('category'), 'section': sidebarF.get('section'),'blog':all, }
    return render(response, 'blog/blogdetail.html', context)