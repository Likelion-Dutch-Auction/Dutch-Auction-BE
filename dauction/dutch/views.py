import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Ad, Proposal

def create_ad(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        title = data.get('title')
        content = data.get('content')
        minimum_price = data.get('minimum_price')

        ad = Ad(
            title=title,
            content=content,
            minimum_price=minimum_price
        )
        ad.save()
        return JsonResponse({'message': 'success'})
    return JsonResponse({'message': 'POST 요청만 허용됩니다.'}, status=400)