import base64
from django.core.files.base import ContentFile
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Documents
from .serializers import DocumentsSerializer
from django.http import FileResponse
from django.views import View
from pathlib import Path
import json
import os

BASE_DIR = Path(__file__).resolve().parent.parent


class FileDownloadView(View):
    def get(self, request, file_path):
        file_path = os.path.join(BASE_DIR, 'media/media/', file_path)  # Replace with the actual path to your files
        response = FileResponse(open(file_path, 'rb'))
        return response


class DocumentsListCreateView(generics.ListCreateAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer

    def create(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))

        doc_base64 = data.pop('doc', '')  # Assuming 'doc_base64' is the key for base64-encoded file
        doc_name = data.pop('doc_name', '')  # You may want to pass the file name in the request

        try:
            if doc_base64 != '':
                # Decode the base64 string to bytes
                doc_bytes = base64.b64decode(doc_base64)

                # Save the file to your storage
                doc_content = ContentFile(doc_bytes, name=doc_name)

                # Add the file to the request data
                data['doc'] = doc_content

            # Call the original create method
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            # Return the response similar to super().create
            headers = self.get_success_headers(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Convert 'doc' field to base64 in each message
        for message in serializer.data:
            if message['doc']:
                doc_path = os.path.join(BASE_DIR, 'media/media/', str(message['doc'].split('/')[5]))  # Assuming 'media' is your media root
                try:
                    with open(doc_path, 'rb') as doc_file:
                        doc_content = base64.b64encode(doc_file.read()).decode('utf-8')
                        message['doc_name'] = message['doc'].split('/')[5]
                        message['doc'] = doc_content
                except Exception as e:
                    print(f"Error reading file {doc_path}: {e}")

        return JsonResponse(serializer.data, safe=False)


class DocumentsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer

    def update(self, request, *args, **kwargs):
        if 'doc' in request.data:
            doc_name = request.data.pop('doc_name', '')
            print(doc_name)
            doc_base64 = request.data['doc']
            try:
                doc_content = ContentFile(base64.b64decode(doc_base64), name=doc_name)
                request.data['doc'] = doc_content
            except Exception as e:
                return Response({'error': f'Error decoding base64: {str(e)}'}, status=400)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)
        updatedDocument = serializer.data
        if updatedDocument['doc']:
            doc_path = os.path.join(BASE_DIR, 'media/media/', self.get_object().doc.name.split('/')[-1])  # Assuming 'media' is your media root
            try:
                with open(doc_path, 'rb') as doc_file:
                    doc_content = base64.b64encode(doc_file.read()).decode('utf-8')
                    updatedDocument['doc_name'] = updatedDocument['doc'].split('/')[5]
                    updatedDocument['doc'] = doc_content
            except Exception as e:
                print(f"Error reading file {doc_path}: {e}")

        return Response(updatedDocument)
