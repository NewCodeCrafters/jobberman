from rest_framework import views, status, response
from job.serializers import SkillSerializer, JobSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import response, status, permissions, views
from .models import Job


class AddSkillView(views.APIView):
    serializer_class = SkillSerializer
    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"success": "Skill Successfully saved"}, status=status.HTTP_201_CREATED)
        return response.Response({"error": "Skill not saved"}, status=status.HTTP_400_BAD_REQUEST)
    
    
class PostJobView(views.APIView):
    serializer_class = JobSerializer

    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"success": "Job Successfully saved"}, status=status.HTTP_201_CREATED)
        return response.Response({"error": "Job not saved"}, status=status.HTTP_400_BAD_REQUEST)
    





class GetUpdateJobView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = JobSerializer


    def get(self, request):
        user = request.user
        jobs = Job.objects.get(user=user)
        serializer = JobSerializer(jobs)
        return response.Response(serializer.data)

    @swagger_auto_schema(request_body=JobSerializer)
    def put(self, request):
        user = request.user
        jobs = Job.objects.get(user=user)
        serializer = JobSerializer(jobs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
