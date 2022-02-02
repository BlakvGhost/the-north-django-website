from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from .forms import ForumForm
from .models import ForumModel,PubTags
from comments.models import LesCommentaires
from comments.forms import CommentForm

# Create your views here.


def boucle(number):
    i = 1
    context = []
    while i <= number:
        context.append(i)
        i += 1
    return context


def pagine(obj, per_page, page_num=1):
    if page_num is None:
        page_num = 1
    else:
        page_num = int(page_num)
    pagination = Paginator(obj, per_page)
    if page_num > pagination.num_pages:
        page_num = pagination.num_pages
    post = pagination.get_page(page_num)
    totalPage = boucle(pagination.num_pages)
    context = {'post': post, 'totalPage': totalPage}
    return context


def total_comments(posts, comments):
    total = []
    for post in posts:
        objTotal = comments.objects.filter(comment_to=post.id).count()
        total.append([post.id, objTotal])
    return total
def populartags(model):
    tags = PubTags.objects.all()
    NbTags = []
    for tag in tags:
        objTotal = model.objects.filter(pub_tags=tag.id).count()
        if not NbTags.__contains__([tag.tag, objTotal]):
            NbTags.append([objTotal,tag.tag])
    NbTags.sort(reverse=True)
    context = NbTags[0:5]
    return context

def sidebar(model,section="Forum"):
    postBar = model.objects.all().order_by('-id')[:3]
    categoryBarNb = []
    tags = populartags(model)
    for category in model.objects.all():
        objTotal = model.objects.filter(pub_categorie=category.pub_categorie).count()
        if not categoryBarNb.__contains__([category.pub_categorie, objTotal]):
            categoryBarNb.append([category.pub_categorie, objTotal])
    context = {'postBar':postBar,'category':categoryBarNb,'stags':tags,'section':section}
    return context

def forum(request):
    if not request.user.is_authenticated:
        return redirect('connexion')
    else:
        if request.method == 'POST':
            forms = ForumForm(request.POST)
            if forms.is_valid():
                articles = forms.save(commit=False)
                articles.pub_author = request.user
                articles.save()
        else:
            forms = ForumForm
        forumPost = ForumModel.objects.all().order_by('-id')
        page = pagine(forumPost, 10, request.GET.get('p'))
        totalComments = total_comments(forumPost, LesCommentaires)
        sidebarF = sidebar(ForumModel)
        context = {'forumPost': page.get('post'), 'forumForm': forms, 'page': page.get('totalPage'),
                   'posts': sidebarF.get('postBar'),'stags': sidebarF.get('stags'),'section':sidebarF.get('section'),
                   'category':sidebarF.get('category'), 'totalComments': totalComments}
        return render(request, 'forum/forum.html', context)


def details(request, pk):
    if not request.user.is_authenticated:
        return redirect('connexion')
    else:
        if request.method == 'POST':
            forms = CommentForm(request.POST)
            if forms.is_valid():
                commentaire = forms.save(commit=False)
                commentaire.comment_author = request.user
                commentaire.comment_to = pk
                commentaire.comment_categorie = ForumModel.objects.get(
                    id=pk).pub_categorie
                commentaire.comment_type = request.POST.get('commentType')
                commentaire.comment_replyedTo = request.POST.get('replyTo')
                commentaire.save()
        else:
            forms = CommentForm
        forumPost = ForumModel.objects.get(id=pk)
        commentsPost = LesCommentaires.objects.filter(comment_to=pk, comment_type='just comment').order_by(
            '-id')
        commentsReplyPost = LesCommentaires.objects.filter(comment_to=pk, comment_type='Reply').order_by(
            '-id')
        totalComm = commentsPost.count()+commentsReplyPost.count()
        commentsPost = pagine(commentsPost, 5, request.GET.get('p'))
        tags = forumPost.pub_tags.all()
        sidebarF = sidebar(ForumModel)
        context = {'forumPost': forumPost, 'CommentForm': forms, 'commentsPost': commentsPost.get('post'), 'totalComm': totalComm,'stags': sidebarF.get('stags'),
                   'tags': tags, 'page': commentsPost.get('totalPage'), 'Reply': commentsReplyPost,
                   'posts': sidebarF.get('postBar'),'category': sidebarF.get('category'),'section':sidebarF.get('section')
                   }
        return render(request, 'forum/forumdetail.html', context)
def category(request,ct):
    if not request.user.is_authenticated:
        return redirect('connexion')
    else:
        #forumPost = ForumModel.objects.filter(pub_categorie=ct).order_by('-id')
        forumPost = ForumModel.pub_categorie
        page = pagine(forumPost, 10, request.GET.get('p'))
        totalComments = total_comments(forumPost, LesCommentaires)
        sidebarF = sidebar(ForumModel)
        context = {'cat':ct,'forumPost': page.get('post'),'page': page.get('totalPage'),
                       'posts': sidebarF.get('postBar'),'stags': sidebarF.get('stags'),'section':sidebarF.get(
                'section'),
                       'category':sidebarF.get('category'), 'totalComments': totalComments}
        return render(request,'forum/category.html',context)

def search(request):
    if not request.user.is_authenticated:
        return redirect('connexion')
    else:
        query = request.GET.get('s')
        sidebarF = sidebar(ForumModel)
        if query is None:
            context = {'empty':"Veillez entrer un mot de recherche",'posts': sidebarF.get('postBar'),'category':sidebarF.get('category')}
        else:
            forumPost = ForumModel.objects.filter(post__icontains=query)
            page = pagine(forumPost, 10, request.GET.get('p'))
            totalComments = total_comments(forumPost, LesCommentaires)
            tg = populartags()
            context = {'cat':query,'forumPost': page.get('post'),'page': page.get('totalPage'),
                           'posts': sidebarF.get('postBar'),'stags': sidebarF.get('stags'),'section':sidebarF.get(
                    'section'),
                           'category':sidebarF.get('category'), 'totalComments': totalComments}
        return render(request,'forum/search.html',context)

def ajax(request):
    query = request.GET.get('s')
    response = ForumModel.objects.filter(post__icontains=query).order_by('-id')
    comments = total_comments(response,LesCommentaires)
    data = {'datas':list(response.values('post')),'comments':comments}
    return JsonResponse(data)