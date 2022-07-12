from django.shortcuts import render, redirect
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.conf import settings

from . import util
from . import urls

import markdown2
import random

def index(request):
    return render(request, 'encyclopedia/index.html', {
        'entries': util.list_entries()
    })

# Manages entry page view
def title(request, title):
    # GET all available entries. returns LIST
    all_entries = util.list_entries()
    filter_list = []

    for item in all_entries:
        if item.lower() == title.lower():
            title = item
            pass

#    del request.session['var']

    request.session['var'] = title

    # Looks for markdown entry. returns STR
    entry = util.get_entry(title)

    if entry != None:
        # debugs creation of new entry markdown format
        # if '"' in entry:
            # entry = entry.replace('"', '')

        # filter converts markdown to html
        html = markdown2.markdown(entry)

        return render(request, 'encyclopedia/title.html', {
            'title': title,
            'data': html
        })

    else:
        raise Http404()

# Manages search page
def search(request):
    if request.method == 'POST':
        entry_list = util.list_entries()

        # lower case entry list
        filter_list = []

        # convert all entries to lower case.
        for entry in entry_list:
            filter_list.append(entry.lower())

        # get query by name of html input tag
        query = request.POST.get('search')

        if query.lower() in filter_list:
            # redirect to wiki/<title>
            return redirect('title', title=query)
        else:
            new_entry_list = []
            for entry in entry_list:
            # search substring of entry
                if query.lower() in entry.lower():
                    new_entry_list.append(entry)

            if new_entry_list:
                return render(request, 'encyclopedia/search.html', {
                    'entries': new_entry_list
                })
            else:
                raise Http404()

def newpage(request):
    if request.method == 'POST':
        entry_list = util.list_entries()
        filter_list = []

        title = request.POST.get('new-entry-title')
        textarea = request.POST.get('textarea')

        for entry in entry_list:
            filter_list.append(entry.lower())

        if title.lower() in filter_list:
            raise PermissionDenied
        else:
            util.save_entry(title, textarea)
            return redirect('title', title=title)
    else:
        return render(request, 'encyclopedia/newpage.html')

# def forbidden(request):
    # return render(request, 'encyclopedia/forbidden.html')

def editpage(request):
    title = request.session.get('var')
    markdown = util.get_entry(title)

    if request.method == 'POST':
        markdown = request.POST.get('textarea')
        util.save_entry(title, markdown)

        return redirect('title', title=title)

    else:
        return render(request, 'encyclopedia/editpage.html', {
            'title': title,
            'data': markdown
        })

def randompage(request):
    entry_list = util.list_entries()
    num = len(entry_list) - 1

    shuffle = random.randint(0, num)

    title = entry_list[shuffle]

    return redirect('title', title=title)
