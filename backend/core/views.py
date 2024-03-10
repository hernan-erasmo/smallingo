from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import SmallingoVideo
from core.serializers import SmallingoVideoSerializer, SmallingoVideoCreateSerializer
from core.utils import format_video_info

class SmallingoVideoListView(APIView):
    def get(self, request):
        videos = SmallingoVideo.objects.all()
        serializer = SmallingoVideoSerializer(videos, many=True)
        return Response(serializer.data)


class SmallingoVideoDetailView(APIView):
    def get(self, request, pk):
        try:
            smallingo_video = SmallingoVideo.objects.get(pk=pk)
            data = format_video_info(smallingo_video)
            return Response(data)
        except SmallingoVideo.DoesNotExist:
            return Response({'error': 'Object does not exist', 'id': -1}, status=status.HTTP_404_NOT_FOUND)


class SmallingoVideoCreateView(APIView):
    def post(self, request):
        serializer = SmallingoVideoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.instance.id}, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid data provided', 'id': -1}, status=status.HTTP_400_BAD_REQUEST)
