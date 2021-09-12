from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy, reverse
from django.contrib import messages

from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, views
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Image, Catagory
from .filters import CatagoryFilter
from .forms import ImageForm
from .permissions import IsOwnerOrReadOnly
from .serializers import CatagorySerializer

from django.db.models import Q

class UserCreateView(CreateView):
    template_name =template_name = 'image_gallery/create_form.html'
    success_url = reverse_lazy('image_gallery:login')
    form_class = UserCreationForm

class HomeView(View):
    model = Image
    template_name = 'image_gallery/home.html'

    def filter_objects(self, request, strval):
        if strval:
            query = Q(owner__first_name__contains=strval)
            query.add(Q(owner__last_name__contains=strval), Q.OR)
            query.add(Q(owner__username__contains=strval), Q.OR)
            query.add(Q(description__contains=strval), Q.OR)
            objects = Image.objects.filter(query).select_related()
        else :
            objects = Image.objects.all()
        return objects  

    def get(self, request):
        strval = request.GET.get('search', False)
        images = self.filter_objects(request, strval)
        myFilter = CatagoryFilter(request.GET, queryset=images)
        images = myFilter.qs

        ctx = {'images':images, 'filter':myFilter}
        return render(request, self.template_name, ctx)

class ImageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'image_gallery/image_create.html'
    success_url = reverse_lazy('image_gallery:home')
    
    def get(self, request):
        form = ImageForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.owner = request.user
            image.save()
            
            return redirect(reverse_lazy('image_gallery:home'))
        return render(request, self.template_name, {'form':form})        

class ImageUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'image_gallery/image_create.html'
    success_url = reverse_lazy('image_gallery:home')

    def get(self, request, pk):
        image = get_object_or_404(Image, id=pk, owner=self.request.user)
        form = ImageForm(instance=image)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        image = get_object_or_404(Image, id=pk, owner=self.request.user)
        form = ImageForm(request.POST, request.FILES, instance=image)

        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect(self.success_url)

        ctx = {'form': form}
        return render(request, self.template_name, ctx)
    
class ImageDetailView(DetailView):
    template_name = 'image_gallery/image_detail.html'
    model = Image

class ImageDestroyView(generics.DestroyAPIView):
    queryset = Image
    permission_classes = [IsOwnerOrReadOnly]

class CatagoryCreateAPIView(generics.CreateAPIView):
    model = Catagory
    fields = '__all__'
    success_url = reverse_lazy('image_gallery:image_create')


class CatagoryCreateAPIView(generics.CreateAPIView):
    queryset = Catagory
    serializer_class = CatagorySerializer
    permission_classes = [IsAuthenticated]
