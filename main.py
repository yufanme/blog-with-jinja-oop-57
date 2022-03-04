from flask import Flask, render_template
import requests
from post import Post

blog_api_url = "https://api.npoint.io/4af156202f984d3464c3"
blog_objects = []
posts = requests.get(url=blog_api_url).json()
for post in posts:
    post_object = Post(post["id"], post["body"], post["title"], post["subtitle"])
    blog_objects.append(post_object)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blog_objects=blog_objects)


@app.route('/post/<int:blog_id>')
def show_post(blog_id):
    request_blog = None
    for blog_object in blog_objects:
        if blog_object.id == blog_id:
            request_blog = blog_object
    return render_template("post.html", blog_object=request_blog)


if __name__ == "__main__":
    app.run(debug=True)
