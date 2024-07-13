from django.http import HttpResponse
#Request: hace una petición de tipo HTTP
#HttpResponse: devuelve una respuesta de tipo HTTP

def holamundo(request):
    return HttpResponse("Hola Mundo")
#Se crea una función que recibe una petición y devuelve un mensaje de respuesta
