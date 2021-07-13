from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
import os

# Create your views here.

def mask(str_u):
    lst_int = [ord(c)+5 for c in str_u] #mask: shift rightward by 5
    lst_chr = [chr(code) for code in lst_int]
    masked = "".join(lst_chr)
    return masked

def unmask(str_m):
    lst_int = [ord(c)-5 for c in str_m] #unmask: shift leftward by 5
    lst_chr = [chr(code) for code in lst_int]
    unmasked = "".join(lst_chr)
    return unmasked

def toSafe(str_unsafe):
    return str_unsafe.replace("<script>", "&ltscript&gt").replace("<script ", "&ltscript ").replace("</script>", "&lt/script&gt" )


# actions

def search_index(request):
    return render(request, 'index.html')

def search_result(request):
    mask: str = "0"
    try:
        mask = request.GET['mask']
    except:
        pass

    keyword: str = ""
    try:
        keyword = request.GET['keyword']
    except:
        pass

    if (mask == "0"):
        htmlFileStr = ""
        if keyword == "":
            htmlFilePath = os.getcwd() + "/search/templates/search_result_none.html"
            htmlFile = open(htmlFilePath, 'r')
            htmlFileStr = htmlFile.read().replace("\n", " ")
            htmlFile.close()
        else: 
            htmlFilePath = os.getcwd() + "/search/templates/search_result.html"
            htmlFile = open(htmlFilePath, 'r')
            htmlFileStr = htmlFile.read().replace("\n", " ").format(keyword_url=toSafe(keyword), keyword=keyword)
            htmlFile.close()
        return HttpResponse(htmlFileStr) 

    else:
        htmlFilePath = os.getcwd() + "/search/templates/search_result_with_link.html"
        htmlFile = open(htmlFilePath, 'r')
        htmlFileStr = htmlFile.read().replace("\n", " ").format(keyword_url=toSafe(keyword), keyword_url_unmasked=toSafe(unmask(keyword)), keyword=unmask(keyword))
        htmlFile.close()
        return HttpResponse(htmlFileStr)




