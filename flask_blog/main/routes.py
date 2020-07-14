from flask import Blueprint, render_template, request
from flask_blog.models import Post

main = Blueprint('main', __name__)


# Basically the root page of the home page
@main.route('/')
@main.route('/home')
def home():
    # Page is looking up the URL for query params
    page = request.args.get('page', 1, type = int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=3, page = page)
    return render_template('home.html', posts = posts)

# Create an about page
@main.route('/about')
def about():
    return render_template('about.html', title = "About")
