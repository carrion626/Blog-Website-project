from flask import Flask, render_template, request
import requests
from post import Post
import sss

app = Flask(__name__)

response = requests.get(sss.url1).json()
name = sss.name1

all_posts = []
for i in response:
    post = Post(id=i['id'], title=i['title'], subtitle=i['subtitle'], body=i['body'])
    all_posts.append(post)


@app.route('/')
def home():
    return render_template('index.html', posts=response, name=name)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        print(data['name'])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
    return render_template("contact.html")


@app.route('/<int:num>')
def post(num):
    required_post = None
    for u in all_posts:
        if num == u.id:
            required_post = u
    return render_template('post.html', required_post=required_post, name=name)


if __name__ == "__main__":
    app.run(debug=True)
