from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status   
from .process_uploaded import process_uploaded_files

@api_view(['POST'])
def update_database(request):
    try:
        # Ensure the file key matches the form field name ('file' instead of 'file.xlsx')
        uploaded_files = request.FILES.getlist('file.xlsx')

        if not uploaded_files:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Call the utility function to process the uploaded files

        responses = process_uploaded_files(uploaded_files)
        ls=responses
        return JsonResponse({"responses": ls})
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
