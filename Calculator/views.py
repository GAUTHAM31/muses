# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import modelconfig
import requests
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


# Load Movies Metadata
metadata = pd.read_csv('movies_metadata.csv', low_memory=False)

m = metadata['vote_count'].quantile(0.90)

q_movies = metadata.copy().loc[metadata['vote_count'] >= m]


#Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
tfidf = TfidfVectorizer(stop_words='english')

#Replace NaN with an empty string
metadata['overview'] = q_movies['overview'].fillna(' ')

#Construct the required TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(q_movies['overview'].values.astype('str'))

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(q_movies.index, index=q_movies['title']).drop_duplicates()

def test():
    i=0;

model_selected=test;

def apitest(request):
    r = requests.get('http://localhost:8000/Calculator/api/', params={"input_json":'jsonsjson'})
    print r;
    return HttpResponse(r)

def index(request):
    return render(request, 'Calculator/index.html' , {'result':""})

def api(request):
    model_selected(request.GET["input_json"])
    return HttpResponse("a");

def run(request):
    if request.method=='POST':
        title=request.POST.get('title')
        reply_list = []
        reply = get_recommendations(title)
        for i in reply:
            reply_list.append(i)
        return HttpResponse(json.dumps({"list":reply_list,"api":"tfidf_imdb"}),content_type="application/json")

def home(request):
    return render(request, 'Calculator/test.html' , {'result':""})

def get_recommendations(title, cosine_sim=cosine_sim):
    title = str(title)
    # Get the index of the movie that matches the title
    idx = indices[title]


    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return q_movies['title'].iloc[movie_indices]

def home_api(request):
    # return HttpResponse("Djangothon");
    function_list= list(modelconfig.models.keys())
    if request.method == 'POST':
        form=request.POST
        output_json= modelconfig.models.get(form['model_selected'])(form['json_input'])
        global model_selected
        model_selected=modelconfig.models.get(form['model_selected']);
        print "*************"
        print model_selected
    else:
        output_json=""

    api_addr=request.build_absolute_uri('/')+reverse(api)[1:]
    context = {
        'functions': function_list,
        'output_json': output_json,
        'link': api_addr
    }
    print reverse('index');
    print request.build_absolute_uri('/')
    print api_addr;
    return render(request, 'Calculator/home.html' , context)
# Create your views here.
