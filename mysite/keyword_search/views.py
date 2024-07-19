from django.shortcuts import render
from django.db.models import Q
from .models import Document 

# Create your views here.
def search_view(request):
    query = request.GET.get('query', '')
    if query:
        # 필드 이름 확인 
        results = Document.objects.filter(
            Q(word__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        results = Document.objects.none()
    # 검색 기능에 필요한 로직을 구현하고 결과를 템플릿으로 전달
    # 예시로 render 함수를 사용하여 템플릿을 렌더링한다.
    return render(request, 'search_results.html', {'results': results, 'query': query})