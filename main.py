from flask import Flask,redirect,url_for,render_template
import random
import datetime

init_date_time = str(datetime.datetime.now()).split()[0]

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def home_page():
    articles = []
    return render_template('home.html' , title = 'home')

@app.route('/random_science/')
def rnsa():
    db = (open('C:\\Users\\kais\\Desktop\\Direkt AUS C-137\\data\\db.csv').read().split('\n'))
    articles = []
    for comb in db:
        try:
            comb = comb.split('|')
            print(comb)
            link = comb[0]
            title = comb[1]
            src = comb[2] + '.png'
            name = comb[3]
            article = [link , title , src , name]
            articles.append(article)
        except :
            pass
    random.shuffle(articles)
    return render_template('rnsa.html' , title = 'Random Science' , db = articles)

@app.route('/random_scientific_videos/')
def rsv():
    pass


@app.route('/algerian_newspapers/')
def an():
    db = (open('C:\\Users\\kais\\Desktop\\Direkt AUS C-137\\dzdata\\db.csv').read().split('\n'))
    articles = []
    for comb in db:
        try:
            comb = comb.split('|')
            print(comb)
            link = comb[0]
            title = comb[1]
            src = comb[2] + '.png'
            name = comb[3]
            article = [link , title , src , name]
            articles.append(article)
        except :
            pass
    random.shuffle(articles)
    return render_template('an.html' , title = 'Algerian Newspapers' , db = articles)



if __name__ == '__main__':
    app.run(debug=True)