from django.http import HttpResponse
import TwitterTool
def index(request):
    TwitterTool.Run()
    return HttpResponse("Tweet Collection Successfully Completed!")
