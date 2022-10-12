from django.shortcuts import render, HttpResponse


def meet(request):
    return HttpResponse('Meeting Room')
