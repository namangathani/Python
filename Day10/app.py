from flask import Flask, render_template
from scrape_imdb.imdb_scrape import get_movies_paged

app = Flask(__name__)

@app.route("/")
def func():
    s = get_movies_paged(page=1, movies_per_page=10)
    return render_template("index.html", data=s)

if __name__ == "__main__":
    app.run(debug=True, port=4000)

# from flask import Flask, render_template
# from scrape_imdb.imdb_scrape import get_movies_paged

# app = Flask(__name__)


# @app.route("/nam")
# def hello_world():
#     s = get_movies_paged(page=1, movies_per_page=5)
#     return render_template("index.html", data=s)


# if __name__ == "__main__":
#     app.run(debug=True, port=8000)
