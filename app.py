from flask import *
import pickle
import os
import re
from newsapi import NewsApiClient

app=Flask(__name__)
model=pickle.load(open('goldnewsanalysis.pkl','rb'))

@app.route('/',methods=['POST', 'GET'])
def homepage():
    return render_template('index.html')

@app.route('/prediction',methods=['POST', 'GET'])
def predictionpage():
    if request.method == 'POST':
        newsline = request.form["newheadline"]
        addednewsheadline=newsline
        # if(newsline == ""):
        #     return render_template('index.html', input=0)    
            # return redirect(url_for('home', input=0))    
        pred=[newsline]
        output=model.predict(pred)
        print(output)
        if output==['positive']:
            return render_template('index.html',output='upward movement in gold price' ,newsline=addednewsheadline)
        if output==['negative']:
            return render_template('index.html',output='downward movement in gold price',newsline=addednewsheadline)
        if output==['neutral']:
            return render_template('index.html',output='steady movement in gold price',newsline=addednewsheadline)
        if output==['none']:
            return render_template('index.html',output='this news headline is not related to gold news',newsline=addednewsheadline)
    return render_template('index.html')


@app.route('/news')
def newspage():
    newsapi=NewsApiClient(api_key="43ffea2aa8d84b4fbbe2fe18538d8fa7")
    # topheadlines=newsapi.get_top_headlines(sources='bbc-news')
    topheadlines=newsapi.get_everything(q='Gold')
    toparticles=topheadlines['articles']
    news=[]
    desc=[]
    image=[]
    url=[]
    # print(url)
    # toparticles = str(toparticles)
    # print(toparticles)
    for i in range(len(toparticles)):
        # print(len(toparticles))
        # print(toparticles[i]['title'])
        # if 'Gold' in toparticles['title'] or 'Gold' in toparticles['description']:
        if 'Gold ' in toparticles[i]['title'] or 'Gold' in toparticles[i]['description']:
            mainarticle=toparticles[i]
            news.append(mainarticle['title'])
            desc.append(mainarticle['description'])
            image.append(mainarticle['urlToImage'])
            url.append(mainarticle['url'])
            contents=zip(news,desc,image,url)
            # print(mainarticle)
            if i >= 4:
                break    
    return render_template("index.html",contents=contents)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')