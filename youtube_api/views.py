from django.http import HttpResponse
from django.core.paginator import Paginator
from django.http import JsonResponse

from .autojob import query, run_background_task

from rest_framework import generics
from rest_framework.pagination import CursorPagination
from .models import Video

from django.shortcuts import render
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


from youtube_api.models import Video


def home(request):
    return HttpResponse("Hello, Django!")
    
def get_videos(request):
    try:

        run_background_task()

        # retrieve query parameters for search query, page number, and page size
        # search_query = request.GET.get('query', '')
        # page_num = int(request.GET.get('page', 1))
        # page_size = int(request.GET.get('size', 10))

        search_query = query
        page_num = 1
        page_size = 25
        page_size_query_param = 'page_size'
        max_page_size = 100

        # fetch the videos from the database
        videos = Video.objects.filter(title__contains=search_query, description__contains=search_query)
        print(videos)
        paginator = Paginator(videos, page_size)

        # return a paginated response
        response = {
            'videos': list(paginator.page(page_num).object_list.values()),
            'count': videos.count(),
            'num_pages': paginator.num_pages,
        }
        return JsonResponse(response)
    except Exception as e:
        print(e)



# class ResultsPagination(CursorPagination):
#     page_size = 25
#     page_size_query_param = 'page_size'
#     max_page_size = 100

# class YoutubeItems(generics.ListAPIView):
#     search_fields = ['title', 'description']
#     filter_backends = (filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter)
#     filterset_fields = ['channel_id','channel_title']
#     ordering = ('-publishedDateTime')
#     queryset = Video.objects.all()
#     pagination_class = ResultsPagination
