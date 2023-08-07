from django.shortcuts import render, redirect


def displayindex(request):
    return render(request, "index.html")


def displayshop(request):
    return render(request, "shop.html")


def displaywhy(request):
    return render(request, "why.html")
