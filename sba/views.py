from django.http import HttpResponse
import TwitterTool
def index(request):
    TwitterTool.Run()
    return HttpResponse("Hello, world. You're at the tweetz index.")# Create your views here.# Create your views here.
