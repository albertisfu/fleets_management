from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Paginar
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.views.decorators.csrf import csrf_protect 

from management.models import Vehicle

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.contrib.auth import logout


@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid username and password'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/login')


# Create home
@method_decorator(login_required, name='dispatch')
class home(ListView):
    """ Listar slider inicio """
    model = Vehicle
    template_name = 'home.html'
    paginate_by = 100  # Elementos por pagina
    ordering = ['-vehicle_id']

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        lista = Vehicle.objects.all()
        paginator = Paginator(lista, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            list_s = paginator.page(page)
        except PageNotAnInteger:
            list_s = paginator.page(1)
        except EmptyPage:
            list_s = paginator.page(paginator.num_pages)

        context['lista'] = list_s
        return context


@login_required(login_url='/login')
def detail_vehicle(request, pk):

    vehicle = Vehicle.objects.get(pk=pk)

    history = vehicle.get_vehicle_history

    paginate_by = 20
    paginator = Paginator(history, paginate_by)
    page = request.GET.get('page')

    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)


    return render(
        request=request,
        template_name='detail_vehicle.html',
        context={
            'vehicle': vehicle, 
            'history': objects})