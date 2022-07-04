from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    mensaje="""
    <h1>Universidad Nacional de Lima Sur<br/>EP Ingenieria de Sistemas<br/>Bienvenidos</h1>
    """
    return HttpResponse(mensaje)
    
def UC3(request):
    mensaje="""
    <h3>Lenguaje de Programación III <br/> Evaluación de la Unidad de Competencia 3</h3>
    <p>Docente: Mg. Flor Elizabeth Cerdán León <br/> Integrantes: 
    <ol>
        <li>Ruiz Montero Carlos Alberto
        <li>Vasquez Leyva Antony
        <li>Zevallos Torres Diego Leonel
    </ol>
    </p>
    """
    return HttpResponse(mensaje)

def noticia(request):
    mensaje="""
    <h2>Paro nacional Afecta todo Perú</h2>
    <p>Para mas información <A HREF="https://elcomercio.pe/respuestas/paro-de-transportistas-del-lunes-4-de-julio-en-lima-y-callao-que-se-sabe-medidas-y-ultima-hora-de-las-protestas-paro-nacional-mtc-tdex-revtli-lbposting-noticia/"> CLIK AQUI </A></p></br>
    <img src="https://elcomercio.pe/resizer/diR_zuJcyOgbkOe0x0LvdHwjCJE=/787x442/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/MTXP3QMJMFBOFO2LLRWDX4QUOA.jpg">
    """
    return HttpResponse(mensaje)