
### Django default
from django.http import JsonResponse, HttpResponse,response
from django.shortcuts import render
### DJANGO REST FRAMEWORK ###
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
### Model ###
from django.contrib.auth.models import User, Group
from .models import Person
### Serializers ###
from .serializers import UserSerializer, GroupSerializer, GetAllPersonSerializer


#class-based vs function-based
class GetAllPerson(APIView):
    def get(self,request):
        list_person = Person.objects.all()  # trả về danh sách
        mydata = GetAllPersonSerializer(list_person, many=True)  #nhét list_person vào serializer
        return Response(data=mydata.data,status=status.HTTP_200_OK) # Show dữ liệu lên giao diện

class simple(APIView):
    def post(self,request):
        return JsonResponse({"data":[1,2,3,4]})
    def get(self,request):
        return JsonResponse({"data": "Home"})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

def index(request):
    method = request.method.lower()  #chuyển sang chữ lowercase
    if method == "get":
        return JsonResponse({"data" :[1,2,3,4,5]})
    elif method == "post":
        return JsonResponse({"data": "added data successfully"})
    elif method == "put":
        return JsonResponse({"data": "update data successfully"})
    return JsonResponse( {"error": "method not allow"})
#Hiển thị ra template
posts = [
    {
        'author' : 'Van Phu',
        'title' : 'art of love',
        'content' : 'content 1',
        'date_posts': 'December 27, 1996'
    },
    {
        'author' : 'Nguyen Chuong',
        'title' : 'fly to the sky',
        'content' : 'content 2',
        'date_posts': 'December 28, 1997'
    }
]
def showTemplate(request):
    context = {
        'data_context' : posts,
        'title': 'Show Title'
    }
    return render(request, 'hrm/show_template.html' ,context)
