from django.views.generic import View
from django.shortcuts import render
from .models import Bio


class ShowBioView(View):

    template_name = 'hello/index.html'

    def get(self, request):
        bio = Bio.objects.get(pk=1)
        return render(request, self.template_name, {'bio': bio})
