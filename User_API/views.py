from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializers
from .serializers import *
from .models import *

from .forms import User_form



def User(request):
    form = User_form(request.POST)
    context = {"form":form}
    if form.is_valid():
        form.save()

    return render(request,"user.html",context)


class user_get(APIView):

    def get(self,request):

        user = User_Profile.objects.all()
        serilizer = UserSerializers(user,many=True)
        return Response(serilizer.data)