from django.http import HttpResponse

def index(request):
    linkStr_S = '<a href="../">'
    linkStr_Msg = 'Go to main page'
    linkStr_E = '</a>'
    return HttpResponse('Rango says here is the about page<br>'+linkStr_S + linkStr_Msg + linkStr_E)