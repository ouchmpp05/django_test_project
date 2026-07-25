# board/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

# 1. 게시글 목록 조회 API (GET)
@api_view(['GET'])
def post_list_api(request):
    posts = Post.objects.all().order_by('-created_at') # 최신순으로 가져오기
    serializer = PostSerializer(posts, many=True) # 데이터가 여러 개(many=True)일 때 통역!
    return Response(serializer.data) # JSON으로 변환된 데이터를 쏩니다.

# 2. 게시글 작성 API (POST)
@api_view(['POST'])
def post_write_api(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid(): # 데이터가 형식에 맞는지 꼼꼼히 검사
        serializer.save() # 통과하면 DB에 안전하게 저장
        return Response({"message": "게시글 작성 성공!", "data": serializer.data}, status=201)
    return Response(serializer.errors, status=400) # 틀렸으면 에러 리턴