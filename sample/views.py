from django.shortcuts import render
import os
from django.views.generic.base import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


class Sample(TemplateView):
    template_name = 'sample.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Sample, self).get_context_data(*args, **kwargs)
        context['message'] = 'Hello World!'
        context['cal'] = "Temp"
        context['title'] = "Yeda"
        return context


@api_view(["POST"])
def temp_endpoint(request):
    print("ID : " + str(request.GET.get("id")))
    return Response(dict({"message": "success"}))


@api_view(["POST"])
def temp_template(request):
    print("First Name : " + str(request.data["fname"]))
    print("Last Name : " + str(request.data["lname"]))
    print("score_id : " + str(request.data["score_id"]))
    return render(request, "new.html", context={"fname": request.data["fname"], "lname": request.data["lname"]})


class MockService(object):
    def __init__(self):
        self.am = "Aditya Mehta"

    def print_name(self):
        return self.am

    def diff_method(self):
        return 1234
