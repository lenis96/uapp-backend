from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework import status
from apps.accounts.api.serializers import UserSerializer

# class MyProfile(viewsets.ViewSet):
#     def 

class MyProfileAPIView(views.APIView):
    def get(self,request,version):
        if request.user.is_authenticated:
            data = UserSerializer(request.user).data
            return Response(data)
        else:

            return Response(status=status.HTTP_401_UNAUTHORIZED)