# 파이썬 내장 함수
import json

# pip로 설치한 서드파티 패키지
from django.http import JsonResponse
from django.views import View

# 내가 직접만든 코드
from owners.models import Owner, Dog

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner1 = Owner.objects.create(name=data['owner_name'], email=data['email'], age=data['owner_age'])
        return JsonResponse({'message':'created'}, status=201)


class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        dog1 = Dog.objects.create(owner=Owner.objects.get(name=data['owner_name']), name=data['dog_name'], age=data['dog_age'])
        return JsonResponse({'message':'created'}, status=201)