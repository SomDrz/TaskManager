# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializer import TaskSerializer

@api_view(['GET', 'POST'])


#create and get apis
def taskCreate(request):
    if request.method == 'GET':
        queryset = Task.objects.all()
        title = request.GET.get('title')
        date = request.GET.get('date')
        sort  = request.GET.get('sortdate')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if date:
            queryset = queryset.filter(date=date)
        if sort and sort.lower() == "true":
            queryset = queryset.order_by("date")

        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#update api
@api_view(['PATCH'])
def taskUpdate(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
#delete api
@api_view(['DELETE'])
def taskDelete(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)