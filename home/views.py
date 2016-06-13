from chef_browser import app 
from flask import render_template, redirect, session, request, url_for, flash
from blog.models import Blog, Post, Category

POSTS_PER_PAGE = 5

@app.route('/home_build')
@app.route('/home_build/<int:page>')
def home_build(page=1):
    
    blog = Blog.query.first()
    posts = Post.query.filter_by(live=True).order_by(Post.publish_date.desc()).paginate(page, POSTS_PER_PAGE, False)
    
    return render_template('home/home_page/index.html', blog=blog, posts=posts)