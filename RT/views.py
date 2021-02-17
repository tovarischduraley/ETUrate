from django.http import HttpResponse


def index(request):
    return HttpResponse("Here's the text of the Web page.")