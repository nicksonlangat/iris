import os
from pathlib import Path
from llama_index import GPTVectorStoreIndex, download_loader
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import serializers
from .models import Document
from django.conf import settings

os.environ['OPENAI_API_KEY'] = settings.OPENAI_KEY

def prepare_json_index(file):
    JSONReader = download_loader("JSONReader")
    loader = JSONReader()
    documents = loader.load_data(Path(file))
    index = GPTVectorStoreIndex.from_documents(documents)
    return index

def prepare_word_index(file):
    DocxReader = download_loader("DocxReader")
    loader = DocxReader()
    documents = loader.load_data(file=file)
    index = GPTVectorStoreIndex.from_documents(documents)
    return index

def prepare_pdf_index(file):
    PDFReader = download_loader("PDFReader")
    loader = PDFReader()
    documents = loader.load_data(file=file)
    index = GPTVectorStoreIndex.from_documents(documents)
    return index

class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ["id", "name", "type", "file", "created", "modified"]

class HomeView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        data = request.data
        serializer = FileSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"success": serializer.data})
        
    def get(self, request, format=None):
        documents = Document.objects.all()
        serializer = FileSerializer(documents, many=True)

        return Response({
            "documents": serializer.data
        })


class ChatView(APIView):
    authentication_classes = []
    permission_classes = []
        
    def get(self, request, format=None):
        prompt = request.query_params.get('prompt')
        file = request.query_params.get('file')

        saved_file = Document.objects.get(name=file)
        path = f'{settings.MEDIA_ROOT}/{saved_file.file}'

        if saved_file.type == 'json':
            query_engine = prepare_json_index(path).as_query_engine()

        elif saved_file.type == 'word':
            query_engine = prepare_word_index(path).as_query_engine()

        elif saved_file.type == 'pdf':
            query_engine = prepare_pdf_index(path).as_query_engine()

        response = query_engine.query(prompt)
        
        return Response({
            "prompt": prompt,
            "response": str(response)
        })
