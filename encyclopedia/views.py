from django.shortcuts import render
from django.http import HttpResponseRedirect
import markdown2
from django import forms
from django.urls import reverse
import random
from . import util
from django.shortcuts import redirect

class NewArticleForm(forms.Form):
    title = forms.CharField(label="Title:")
    content = forms.CharField(label="Content:", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write in markdown(.md)', 'style': 'width: 95%; margin-bottom:10px;'}))

def random_entry(request):
    all = util.list_entries()
    if not all:
        return redirect('index') 
    
    rndm = random.choice(all)
    return redirect('entry', rndm.lower())  

def change(request, title):
    if request.method == "POST":
        form2 = NewArticleForm(request.POST)

        if form2.is_valid():
            title = form2.cleaned_data["title"]
            content = form2.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", kwargs={"title": title}))
        else:
            return render(request, "encyclopedia/changeentry.html", {
                "form2": form2, 
                "title": title.capitalize()
            })

    contenttoedit= util.get_entry(title)
    return render(request, "encyclopedia/changeentry.html", {
        "form2": NewArticleForm(initial={'title': title, 'content': contenttoedit}),
        "title": title.capitalize()
    })

def add(request):
    if request.method == "POST":
        form1 = NewArticleForm(request.POST)

        if form1.is_valid():
            title = form1.cleaned_data["title"]
            content = form1.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", kwargs={"title": title}))
        else:
            return render(request, "encyclopedia/newPage.html", {
                "form1": form1
            })

    return render(request, "encyclopedia/newPage.html", {
        "form1": NewArticleForm()
    })

def search_redirect(request):
    search_term = request.GET.get('q', '')
    search_term= search_term.lower()
    x = util.get_entry(search_term)
    
    if x is None: 
        #it was mentioned in the specifiacation of the project that if there is no such entry, when searched for....
        # then display a list of all encyclopedia entries that have the query as a substring.
        # BUT when that same substring is visited using /wiki/TITLE in the URL section,  then there just should be a single messege of entry not found.
        #so two code for both cases are written separately
        articles = util.list_entries()
        possible_results = []
        
        for article in articles:
            if search_term in article.lower():
                possible_results.append(article)
        
        return render(request, "encyclopedia/querynotfound.html", {  
            'search_term': search_term.capitalize(),
            'possible_results': possible_results
        })
    else:
        return redirect('entry', search_term.lower())

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
