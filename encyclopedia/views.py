from django.shortcuts import render
from django.http import HttpResponse
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    x= util.get_entry(title)
    if x==None:
        return render(request, "encyclopedia/no_entry.html")

    html_content = markdown2.markdown(x)
        
    return render(request, "encyclopedia/entry.html", {
        "title": title.capitalize(),
        "html_content" : html_content
    })
