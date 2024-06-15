from flask import Flask, jsonify, request
import pandas as pd

articles_data = pd.read_csv('articles.csv')
all_articles = articles_data[['url' , 'title' , 'text' , 'lang' , 'total_events']]
liked_articles = []
not_liked_articles = []

app = Flask(__name__)

def assign_val():
    m_data = {
        "url": all_articles.iloc[0,0],
        "title": all_articles.iloc[0,1],
        "text": all_articles.iloc[0,2] or "N/A",
        "lang": all_articles.iloc[0,3],
        "total_events": all_articles.iloc[0,4]
    }
    return m_data

# API to display first article
@app.route("/get-article")
def get_article():
    article_data = assign_val()

    return 'Write code to display the first item in all_articles list'


# API to move the article into liked articles list
@app.route("/liked-article")
def liked_article():
    global all_articles
    article_data = assign.val()
    liked_articles.append(article_data)
    all_articles.drop([0], inplace=True)

    return 'Write code to shift first article into liked_articles list'


# # API to move the article into not liked articles list
@app.route("/unliked-article")
def unliked_article():
    global all_articles
    article_data = assign.val()
    not_liked_articles.append(article_data)
    all_articles.drop([0], inplace = True)
    all_articles = all_articles.reset_index(drop=True)

    return 'Write code to shift first article into not_liked_articles list'


@app.route("/popular_articles")
def popular_articles():
    popular_articles_data = []

    for index, row in output.iterrows():
        _p = {
            "url": all_articles.iloc[0,0],
            "title": all_articles.iloc[0,1],
            "text": all_articles.iloc[0,2] or "N/A",
            "lang": all_articles.iloc[0,3],
            "total_events": all_articles.iloc[0,4]
        }
        popular_articles_data.append(_p)

    return "Top 20 articles using demographic filtering method"

@app.route("/recommended_articles")
def recommended_articles():
    global liked_articles
    col_names=['url', 'title', 'text', 'lang', 'total_events']
    all_recommended = pd.DataFrame(columns=col_names)
    
    for liked_movie in liked_articles:
        output = get_recommendations(liked_articles["title"])
        all_recommended=all_recommended.append(output)

    all_recommended.drop_duplicates(subset=["title"],inplace=True)

    recommended_article_data=[]

    for index, row in all_recommended.iterrows():
        _p = {
            "url": all_articles.iloc[0,0],
            "title": all_articles.iloc[0,1],
            "text": all_articles.iloc[0,2] or "N/A",
            "lang": all_articles.iloc[0,3],
            "total_events": all_articles.iloc[0,4]
        }
        recommended_article_data.append(_p)

    return "Top 10 articles using contenct based filtering method"


# run the application
if __name__ == "__main__":
    app.run()