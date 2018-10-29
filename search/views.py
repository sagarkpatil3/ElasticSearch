# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render

from search.documents import PostDocument
# from search.search import search


def search(request):
    q = request.GET.get('q')

    if q:
        posts = PostDocument.search().query("match_phrase_prefix", text=q)
    else:
        posts = ''

    return render(request, 'search/search.html', {'posts': posts})