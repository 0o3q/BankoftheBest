from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Attend

# Create your views here.
def attend(request):
    if not request.user.is_authenticated:
        return redirect('login')
    attends = Attend.objects
    attends_list = Attend.objects.all().order_by('-created_at')
    paginator = Paginator(attends_list, 10)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)
    return render(request, 'attends/attend.html', {'attends' : attends, 'posts' : posts})

def attend_new(request):
    if not request.user.is_authenticated:
        return redirect('login')
    attend = Attend()
    attend.user = request.user
    attend.attend = request.POST['state']
    if attend.attend == '':
        return redirect('attend')
    attend.created_at = timezone.datetime.now()
    attend.save()
    return redirect('attend')