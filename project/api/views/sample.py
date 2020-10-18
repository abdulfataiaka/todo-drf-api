from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])
def sample_view(request):
    data = dict(
        url=request.path,
        media=request.content_type,
        method=request.method,
        files=request.FILES,
        body=request.POST,
        query=request.query_params,
    )

    return Response(data)
