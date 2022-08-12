from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Board

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    boards = Board.objects
    boards_list = Board.objects.all().order_by('-created_at')
    paginator = Paginator(boards_list, 10)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)
    return render(request, 'home/index.html', {'boards' : boards, 'posts' : posts})

def detail(request, board_id):
    if not request.user.is_authenticated:
        return redirect('login')
    board_detail = get_object_or_404(Board, pk=board_id)

    board_detail.view += 1
    board_detail.save()

    return render(request, 'home/detail.html', {'board' : board_detail})

def create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'home/create.html')

def new(request):
    if not request.user.is_authenticated:
        return redirect('login')
    board = Board()
    board.title = request.POST['title']
    if board.title == '':
        return redirect('create')
    board.body = request.POST['body']
    if board.body == '':
        return redirect('create')
    board.author = request.user
    board.created_at = timezone.datetime.now()
    board.save()
    return redirect('home')

def delete(request, board_id):
    if not request.user.is_authenticated:
        return redirect('login')
    board_delete = get_object_or_404(Board, pk=board_id)
    if request.user != board_delete.author:
        return redirect('home')
    board_delete.delete()
    return redirect('home')