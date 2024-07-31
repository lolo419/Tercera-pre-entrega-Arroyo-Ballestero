from django.http import HttpResponse
def saludo(request):
	return HttpResponse("Hola Django - Coder")

def segundVist(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple ")

def dameElDia(request):
    import datetime
    dia = datetime.datetime.now()
    documentoDeTexto = f"hoy es el dia: <br> {dia}"
    return HttpResponse(documentoDeTexto)