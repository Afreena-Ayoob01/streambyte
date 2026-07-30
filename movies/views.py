from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Movie, Comment, Favorite,Category
from .forms import RegistrationForm,MovieForm,CommentForm


@login_required
@login_required
def home(request):

    # Get all movies
    movies = Movie.objects.all().order_by('-created_at')

    # Get all categories
    categories = Category.objects.all()

    # Get search text
    search_query = request.GET.get('q', '').strip()

    # Get selected category
    category_id = request.GET.get('category', '').strip()


    # =================================
    # SEARCH FILTER
    # =================================

    if search_query:

        movies = movies.filter(
            title__icontains=search_query
        )


    # =================================
    # CATEGORY FILTER
    # =================================

    if category_id:

        movies = movies.filter(
            category_id=category_id
        )


    # =================================
    # FEATURED MOVIE
    # Only show featured movie when
    # there is no search or category filter
    # =================================

    if not search_query and not category_id:

        featured_movie = Movie.objects.all().order_by(
            '-created_at'
        ).first()

    else:

        featured_movie = None


    return render(
        request,
        'index.html',
        {
            'movies': movies,
            'categories': categories,
            'featured_movie': featured_movie,
            'search_query': search_query,
            'selected_category': category_id,
        }
    )

@login_required
def movie_detail(request, movie_id):

    movie = get_object_or_404(
        Movie,
        id=movie_id
    )
    is_favorite = Favorite.objects.filter(
    user=request.user,
    movie=movie
    ).exists()
    comments = movie.comments.all()

    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)

            comment.movie = movie

            comment.user = request.user

            comment.save()

            return redirect(
                'movie_detail',
                movie_id=movie.id
            )

    else:

        form = CommentForm()

    return render(
        request,
        'movie_detail.html',
        {
            'movie': movie,
            'comments': comments,
            'form': form,
            'is_favorite': is_favorite
        }
    )
def edit_comment(request, comment_id):

    comment = get_object_or_404(
        Comment,
        id=comment_id,
        user=request.user
    )

    if request.method == 'POST':

        form = CommentForm(
            request.POST,
            instance=comment
        )

        if form.is_valid():

            form.save()

            return redirect(
                'movie_detail',
                movie_id=comment.movie.id
            )

    else:

        form = CommentForm(
            instance=comment
        )

    return render(
        request,
        'edit_comment.html',
        {
            'form': form,
            'comment': comment
        }
    )

def delete_comment(request, comment_id):

    comment = get_object_or_404(
        Comment,
        id=comment_id,
        user=request.user
    )

    movie_id = comment.movie.id

    if request.method == 'POST':

        comment.delete()

        return redirect(
            'movie_detail',
            movie_id=movie_id
        )

    return render(
        request,
        'delete_comment.html',
        {
            'comment': comment
        }
    )

def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            return render(request,'login.html',{'error': 'Invalid username or password.'})

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def add_movie(request):

    if request.method == 'POST':

        form = MovieForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            movie = form.save(commit=False)

            movie.added_by = request.user

            movie.save()

            return redirect('home')

    else:

        form = MovieForm()

    return render(
        request,
        'add_movie.html',
        {'form': form}
    )

@login_required
def edit_movie(request, movie_id):

    movie = get_object_or_404(
        Movie,
        id=movie_id
    )

    if movie.added_by != request.user:
        return redirect('home')

    if request.method == 'POST':

        form = MovieForm(
            request.POST,
            request.FILES,
            instance=movie
        )

        if form.is_valid():

            form.save()

            return redirect(
                'movie_detail',
                movie_id=movie.id
            )

    else:

        form = MovieForm(
            instance=movie
        )

    return render(
        request,
        'edit_movie.html',
        {'form': form, 'movie': movie}
    )

@login_required
def delete_movie(request, movie_id):

    movie = get_object_or_404(
        Movie,
        id=movie_id
    )

    if movie.added_by != request.user:
        return redirect('home')

    if request.method == 'POST':

        movie.delete()

        return redirect('home')

    return render(
        request,
        'delete_movie.html',
        {'movie': movie}
    )

@login_required
def add_favorite(request, movie_id):

    movie = get_object_or_404(
        Movie,
        id=movie_id
    )

    Favorite.objects.get_or_create(
        user=request.user,
        movie=movie
    )

    return redirect(
        'movie_detail',
        movie_id=movie.id
    )

@login_required
def remove_favorite(request, movie_id):

    movie = get_object_or_404(
        Movie,
        id=movie_id
    )

    Favorite.objects.filter(
        user=request.user,
        movie=movie
    ).delete()

    return redirect(
        'movie_detail',
        movie_id=movie.id
    )

@login_required
def my_favorites(request):

    favorites = Favorite.objects.filter(
        user=request.user
    ).select_related('movie')

    return render(
        request,
        'favorites.html',
        {'favorites': favorites}
    )