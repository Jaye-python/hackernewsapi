import json
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import News
import requests
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.contrib import messages
from .tasks import seedDBTask
from rest_framework.views import APIView
from .serializers import NewsSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404


# Create your views here.

class Home(ListView):
    allow_empty = True
    model = News
    template_name = "news/home.html"
    context_object_name = 'news'
    paginate_by = 25

    def get_queryset(self,):
        type = self.request.GET.get('type')
        filter = self.request.GET.get('filter')
        
        if type:
            queryset = News.objects.filter(type=type)     
        elif filter:
            queryset = News.objects.filter(title__icontains= filter)
        else:
            queryset = News.objects.all()
        return queryset


def seedTheDB(request):

    # TO SEED MY DATABASE (BUT ONLY IF THERE ARE NO OBJECTS THEREIN)
    
    
    if News.objects.exists():
        messages.warning(request, 'Database already seeded!')
        pass
    
    else:
        messages.success(request, 'Database is being seeded in the background. Please refresh subsequently. Thank you')

        # RUN TASK WITH 'celery -A hackernews worker -l info'

        seedDBTask.delay()
        
    return redirect ('/')


class NewsDetail( DetailView):
    model = News
    template_name = "news/home.html"
    context_object_name = 'newsdetails'


def deleteNews(request, hacker_id):
    try:
        news = get_object_or_404(News, hacker_id=hacker_id, api_created=True) 
    except:
        messages.warning(request, "This wasn't created via API or this news item does not exist. It may not be deleted. Thank you")
        return redirect ('/')

    if request.method == 'GET':
        return render (request, 'news/news_confirm_delete.html',)
    else:
        news.delete()
        messages.success(request, "News item was deleted successfully!")   
     
    return redirect ('/')


class NewsApi(APIView, LimitOffsetPagination):
    """
    Examples:
    IN JSON FORMAT
    http://127.0.0.1:8000/newsapi/?type=story
    http://127.0.0.1:8000/newsapi/?descendants=1
    http://127.0.0.1:8000/newsapi
    http://127.0.0.1:8000/newsapi/315/          FOR DELETE AND PUT REQUESTS
    """
    

    def get(self, request, format=None):

        # AVAILABLE FILTERS
        hacker_id = self.request.GET.get('id')
        story_type = self.request.GET.get('type')
        descendants = self.request.GET.get('descendants')
        creator = self.request.GET.get('creator')
        
        
        if hacker_id:
            try:
                news = News.objects.get(hacker_id = hacker_id)
                serializer = NewsSerializer(news)
            except News.DoesNotExist:
                raise Http404
        elif story_type:
            try:
                news = News.objects.filter(type=story_type)
                serializer = NewsSerializer(news, many=True)
            except News.DoesNotExist:
                raise Http404
        elif descendants:
            try:
                news = News.objects.filter(descendants=descendants)
                serializer = NewsSerializer(news, many=True)
            except News.DoesNotExist:
                raise Http404
        elif creator:
            try:
                news = News.objects.filter(creator=creator)
                serializer = NewsSerializer(news, many=True)
            except News.DoesNotExist:
                raise Http404
        else:
            try:
                news = News.objects.all()
                serializer = NewsSerializer(news, many=True)
            except News.DoesNotExist:
                raise Http404
        return Response(serializer.data)
    

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.validated_data['api_created'] = True   # Set this db object as api_created to permit delete request 
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk):
        news = News.objects.get(pk=pk)

        if news.api_created:
            serializer = NewsSerializer(news, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request, pk):
        news = News.objects.get(pk=pk)

        if news.api_created:
            news.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)