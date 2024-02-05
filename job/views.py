from rest_framework import views, status, response
from job.serializers import SkillSerializer, JobSerializer
from drf_yasg.utils import swagger_auto_schema


class PostJobView(views.APIView):
    serializer_class = JobSerializer

    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get("title")
            company = serializer.validated_data.get("company")
            work_type = serializer.validated_data.get("work_type")
            job_type = serializer.validated_data.get("job_type")
            description = serializer.validated_data.get("description")
            skills = serializer.validated_data.get("skills")
            serializer.save()
            return response.Response({"success": "Job Successfully saved"}, status=status.HTTP_201_CREATED)
        return response.Response({"error": "Job not saved"}, status=status.HTTP_400_BAD_REQUEST)
    



class AddSkillView(views.APIView):
    serializer_class = SkillSerializer
    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"success": "Skill Successfully saved"}, status=status.HTTP_201_CREATED)
        return response.Response({"error": "Skill not saved"}, status=status.HTTP_400_BAD_REQUEST)