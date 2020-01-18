from django.shortcuts import render

# Create your views here.


def Home(request):

    context = {}
    context["messages"] = "hello wolrd"
    return render(request, "index.html", context)
