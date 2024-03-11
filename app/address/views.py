from django.http import JsonResponse
from django.utils.translation import activate

from app.address.models import Branch


def get_branches(request):
    branches = Branch.objects.filter(is_active=True)
    language = request.GET.get('lang', 'uz')
    activate(language)
    data = [{'id': a.pk, 'name': a.name, 'longitude': a.longitude, 'latitude': a.latitude} for a in branches]
    return JsonResponse({"data": data})
