from django.views.generic import View
from django.shortcuts import render


class ShowBioView(View):

    template_name = 'hello/index.html'

    def get(self, request):
        return render(request, self.template_name)
