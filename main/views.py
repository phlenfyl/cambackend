from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status, generics

from .models import *
from sermon.models import *
from program.models import *
from .serializers import WeekServiceSerializer, ProgramSerializer, SermonSerializer, AuthorSerializer
# Create your views here.


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_programs': '/',
        'Search by Title': '/program/?title=title_name',
        'Search by Tags': '/program/?tags=tags_name',
        'Search by Date': '/program/?date=date_name',
        'Add': '/program/create',
        'Update': '/program/rud/slug',
        'Delete': '/program/rud/slug'
    }

    return Response(api_urls)

class LimitedMainView(generics.ListAPIView):
    queryset = WeekService.objects.order_by('-created')[:3]
    serializer_class = WeekServiceSerializer
    
class LimitedSermonView(generics.ListAPIView):
    queryset = Sermon.objects.order_by('-created')[:3]
    serializer_class = SermonSerializer
    
class LimitedProgramView(generics.ListAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.filter(display=True)
    # filter_backends = [OrderingFilter]
    ordering_fields = ['-created']  # You can order by any field you want

    def get_queryset(self):
        # Define a dictionary to map categories to their respective filters
        program_filters = {
            'speicalprogram': {'speicalprogram': True},
            'deliverance': {'deliverance': True},
            'counseling': {'counseling': True},
        }

        # Get the program from the URL parameter
        program = self.request.query_params.get('program')

        # Check if the program is valid and filter accordingly
        if program in program_filters:
            return self.queryset.filter(**program_filters[program]).order_by('-created')[:3]
        else:
            return Program.objects.filter(display=True)  # Return an empty queryset for invalid categories
    



class WeeklyListAndCreateView(APIView):
    
    def post(self, request):
        serializer = WeekServiceSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({"msg": "already existed"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
       week = WeekService.objects.all()
       serializer = WeekServiceSerializer(week, many= True)
       return Response(serializer.data, status=status.HTTP_200_OK)
       
    


class WeeklyRUDView(APIView):

    def get(self, request, slug):
        try:
            query_set = WeekService.objects.get(slug=slug)
        except WeekService.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)

        serializer = WeekServiceSerializer(query_set, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, slug):
        try:
            query_Set = WeekService.objects.get(slug=slug)
        except WeekService.DoesNotExist:
           return Response(status= status.HTTP_404_NOT_FOUND)

        serializer = WeekServiceSerializer(query_Set, data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_205_RESET_CONTENT)

        return Response(serializer.errors, status = status.HTTP_405_BAD_REQUEST)

    def patch(self, request, slug):
        try:
            query_Set = WeekService.objects.get(slug=slug)
        except WeekService.DoesNotExist:
           return Response(status= status.HTTP_404_NOT_FOUND)

        serializer = WeekServiceSerializer(query_Set, data= request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_205_RESET_CONTENT)

        return Response(serializer.errors, status = status.HTTP_405_BAD_REQUEST)
    
    def delete(self, request, slug):
        try:
            query_Set = WeekService.objects.get(slug=slug)
        except WeekService.DoesNotExist:
           return Response(status= status.HTTP_404_NOT_FOUND)
        
        query_Set.delete()
        return Response({"msg":"Successfully deleted"}, status = status.HTTP_204_NO_CONTENT)


