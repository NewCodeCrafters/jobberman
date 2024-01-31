from django.shortcuts import render
from rest_framework import response, status, permissions, views

from .models import Profiles
from .serializers import ProfileSerializer


class UpdateProfileView(views.APIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            profile = Profiles.objects.get(
                user=request.user
            )
        except Profiles.DoesNotExist:
            return response.Response(
                {"error": "User Profile not Created"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProfileSerializer(profile)
        data = serializer.data
        return response.Response(data, status=status.HTTP_200_OK)

    def put(self, request):
        try:
            profile = Profiles.objects.get(
                user=request.user
            )
        except Profiles.DoesNotExist:
            return response.Response(
                {"error": "User Profile not Created"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    