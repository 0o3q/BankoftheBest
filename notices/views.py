from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .models import Notice

# Create your views here.
def notice(request):
    if not request.user.is_authenticated:
        return redirect('login')
    notices = Notice.objects
    notices_list = Notice.objects.all().order_by('-created_at')
    paginator = Paginator(notices_list, 10)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)
    return render(request, 'notices/notice.html', {'Notices' : notices, 'posts' : posts})

def notice_detail(request, board_id):
    if not request.user.is_authenticated:
        return redirect('login')
    notices_detail = get_object_or_404(Notice, pk=board_id)

    notices_detail.hit += 1
    notices_detail.save()
    return render(request, 'notices/notice_detail.html', {'board' : notices_detail})