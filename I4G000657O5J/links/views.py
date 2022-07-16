from django.shortcuts import render

# Create your views here.
from .models import Link
from .models import LinkSerializer
from .models import APIView
from .models import models
#from .models import ActiveLinkManager
#from .models import serializer
from django.views.generic.list import ListAPIView
from django.views.generic.edit import CreateAPIView
from django.views.generic.detail import DetailAPIView
from django.views.generic.edit import UpdateAPIView
from django.views.generic.edit import DeleteAPIView

class PostListApi(ListAPIView):
    queryset = Link.object.filter(active=True) 
    serializer_class = LinkSerializer
    
class PostCreateApi(CreateAPIView):
    queryset = Link.object.filter(active=True) 
    serializer_class = LinkSerializer
    
  
class PostDetailApi(DetailAPIView):
    queryset = Link.object.filter(active=True) 
    serializer_class = LinkSerializer
    
    
class PostUpdateApi(UpdateAPIView):
   queryset = Link.object.filter(active=True)
   serializer_class = LinkSerializer
    
class PostDeleteApi(DeleteAPIView):
    queryset = Link.object.filter(active=True) 
    serializer_class = LinkSerializer
    
class ActiveLinkView(APIView):
    """
    Returns a list of all active (publicly accessible) links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        qs = models.Link.public.all()
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
class RecentLinkView(APIView):
    """
    Returns a list of recently created active links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = models.Link.public.filter(created_date__gte=seven_days_ago)
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    