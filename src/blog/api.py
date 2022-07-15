from re import S
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


from .models import BlogPost
from .serializers import BlogPostSerializer


# GET /api/blogs
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_blogs(request):
    blogs = BlogPost.objects.all()
    serializer = BlogPostSerializer(blogs, many=True)

    return Response(serializer.data)


# GET /api/blogs/1
@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def get_single_blog(request, id):
    try:
        blog = BlogPost.objects.get(id=id)
    except:
        return Response({'message': f'Blog with id of {id} does not exist.'}, status=404)
    serializer = BlogPostSerializer(blog)
    
    return Response(serializer.data, status=200)


# POST /api/blogs/create
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_blog(request):
    new_blog = JSONParser().parse(request)
    serializer = BlogPostSerializer(data=new_blog)

    # auth_user = User.objects.get(username=request.user.username)
    # # serializer.fields["creator"] = auth_user
    print(request.user)
    if serializer.is_valid():
        serializer.save(creator=request.user)
        return Response(serializer.data, status=201)
    return Response({"message": "Error on creating a new blog", "error": serializer.errors}, status=400)


# DELETE /api/blogs/delete/1
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_blog(request, id):
    try:
        blog = BlogPost.objects.get(id=id)
    except:
        return Response({'message': f'Blog with id of {id} does not exist.'}, status=404)
    
    if not blog.creator == request.user:
        return Response({'message': f'You cannot delete this blog.'}, status=401)        

    blog.delete()

    return Response({'message': f'Blog with id {id} deleted.'}, status=200)


# PUT /api/blogs/update/1
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_blog(request, id):
    try:
        blog = BlogPost.objects.get(id=id)
    except:
        return Response({'message': f'Blog with id of {id} does not exist.'}, status=404)

    if not blog.creator == request.user:
        return Response({'message': f'You are not authorized to update this blog'}, status=401)

    data = JSONParser().parse(request)
    serializer = BlogPostSerializer(blog, data=data)

    if serializer.is_valid():
        serializer.save(creator=request.user)
        return Response(serializer.data, status=201)
    return Response({"message": "Error on updating blog", "error": serializer.errors}, status=400)


