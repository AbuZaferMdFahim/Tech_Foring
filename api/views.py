from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Project, Task, Comment, ProjectMember
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer, CommentSerializer,ProjectMemberSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        data = request.data
        user = User.objects.create_user(
            username=data['username'], 
            email=data['email'], 
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )
        return Response(UserSerializer(user).data)

    @action(detail=False, methods=['post'])
    def login(self, request):
        user = User.objects.filter(username=request.data['username']).first()
        if user and user.check_password(request.data['password']):
            token = RefreshToken.for_user(user)
            return Response({"access": str(token.access_token), "refresh": str(token)})
        return Response({"error": "Invalid credentials"}, status=400)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProjectMemberViewSet(viewsets.ModelViewSet):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
