from django.shortcuts import render
import requests
from .models import Scrapa
from django.http import HttpResponse, JsonResponse
from .serializers import ScrapSerializer
from . import youtube
from rest_framework.decorators import api_view
from rest_framework.response import Response

def scrape_data(request):
    if(request.GET.get('channelid')==None):
        return HttpResponse("Its Blank Here and you are a dumb person")
    
    else:
        channelid=request.GET.get('channelid')
        # result=str(request.GET.get('result'))
        url='https://youtube.googleapis.com/youtube/v3/activities?part=snippet%2CcontentDetails&channelId='+channelid+'&maxResults=24&key=AIzaSyCgTNdaRSwAsHCb6m_rKcUTmEuxjaC8X6U&maxResults=24&type=video'
        # url='https://youtube.googleapis.com/youtube/v3/activities?part=snippet%2CcontentDetails&channelId=UCRWFSbif-RFENbBrSiez1DA&maxResults=25&key=AIzaSyCgTNdaRSwAsHCb6m_rKcUTmEuxjaC8X6U&maxResults=25&type=video'
        
        response = requests.get(url)
        data=response.json()
        for i in range(24):
            try:
                channel_id=data["items"][i]['snippet']['channelId']
                channel_title=data['items'][i]['snippet']['channelTitle']
                title=data['items'][i]['snippet']['title']
                video_id=data['items'][i]['contentDetails']["upload"]['videoId']
                transcript=youtube.get_transcript(video_id)
                published_at=data['items'][i]['snippet']['publishedAt']

                Scrapa.objects.create(channel_id=channel_id,channel_title=channel_title,title=title,video_id=video_id,published_at=published_at,transcript=transcript)
            except KeyError:
                pass

        return HttpResponse("Data Scraped")

@api_view(['GET'])
def get_data(request):
    if(request.GET.get('id')==None):
        data=Scrapa.objects.all()
        serializer=ScrapSerializer(data,many=True)
        return Response(serializer.data)
    
    id=request.GET.get('id')
    print(id) 
    data=Scrapa.objects.filter(id=id)
    serializer=ScrapSerializer(data,many=True)
    return Response(serializer.data) 
# Create your views here.
