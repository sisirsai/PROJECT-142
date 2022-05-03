from flask import Flask,jsonify,request
from storage import all_articles,like_articles,dislike_articles
from demographic_filtering import output
from content_filtering import get_recommendations

app = Flask(__name__)

@app.route('/get-article')

def get_articles():
    return jsonify({
        'data' : all_articles[0],
        'status' : 'success'
    }),200

@app.route('/like-article',methods = ['POST'])

def like_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    like_articles.append(article)
    return jsonify({
        'status' : 'success'
    }),200

@app.route('/dislike-article',methods = ['POST'])

def dislike_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    dislike_articles.append(article)
    return jsonify({
        'status' : 'success'
    }),200

@app.route('/popular-articles')

def popular_articles():
    article_data = []
    for article in output:
        d = {
            "title": article[0], 
            "text": article[1], 
            "url": article[2], 
            "lang": article[3], 
            "contentType": article[4],
            "total events": article[5]
        }
        article_data.append(d)
    return jsonify({
        'data' : article_data,
        'status' : 'success'
    }),200

@app.route('/recommended-articles')

def recommended_articles():
    all_rec = []
    for like in like_articles:
        output = get_recommendations(like_articles[19])
        for data in output:
            all_rec.append(data)

    import itertools

    all_rec.sort() 
    all_rec = list(all_rec for all_rec in itertools.groupby(all_rec)) 
    article_data = []

    for rec in all_rec:
        d = {
            "title": rec[0], 
            "text": rec[1], 
            "url": rec[2], 
            "lang": rec[3], 
            "contentType": rec[4],
            "total events": rec[5]
        }
        article_data.append(d)

    return jsonify({
        'data' : article_data,
        'status' : 'success'
    }),200

if __name__ == '__main__':
    app.run()