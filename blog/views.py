from chef_browser import app
from flask import render_template, redirect, flash, url_for, session, request, abort
from blog.form import SetupForm, PostForm
from chef_browser import db, uploaded_images
from author.models import Author
from blog.models import Blog, Post, Category
from author.decorators import login_required, author_required
import bcrypt
from slugify import slugify
from flask_uploads import UploadNotAllowed

#from flask_mail import Message
from chef_browser import app, mail

import sendgrid

from util import security, send_mail

POSTS_PER_PAGE = 5


@app.route('/blog')
@app.route('/blog/<int:page>')
def blog(page=1):
    
    blog = Blog.query.first()
    posts = Post.query.filter_by(live=True).order_by(Post.publish_date.desc()).paginate(page, POSTS_PER_PAGE, False)
    
    return render_template('blog/blog.html', blog=blog, posts=posts)

@app.route('/blog_admin')
@app.route('/blog_admin/<int:page>')
@login_required
@author_required
def blog_admin(page=1):
    posts = Post.query.order_by(Post.publish_date.desc()).paginate(page, POSTS_PER_PAGE, False)
    return render_template('blog/blog_admin.html', posts=posts)

@app.route('/blog_setup', methods=('GET', 'POST'))
def blog_setup():
    blogs = Blog.query.count()
    #if blogs:
        #return redirect(url_for('blog_admin'))
    form = SetupForm()
    #SetupForm().validate_username(form.username.data)
        
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        author = Author(
            form.fullname.data,
            form.email.data,
            form.username.data,
            hashed_password,
            True
        )
        
        db.session.add(author)
        db.session.flush()
        
        if author.id:
            blog = Blog(form.name.data, author.id)
            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = "Error creating user"
        if author.id and blog.id:
            db.session.commit()
            
            subject = "Confirm your email"
            token = security.ts.dumps("maliksjsu@yahoo.com", salt='email-confirm-key')
    
            confirm_url = url_for(
                'confirm_email',
                token=token,
                _external=True)
        
            html = render_template(
                'email/activate.html',
                confirm_url=confirm_url)
    
            send = send_mail.Message("TELEPORT", form.email.data, "subject", html)
            send.send_message()
            
        else:
            db.session.rollback()
            error = "Error creating blog"
        flash('Blog created')
        
    return render_template('blog/blog_setup.html', form=form)
    

@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = security.ts.loads(token, salt="email-confirm-key", max_age=86400)
    except:
        abort(404)
    
    user = Author.query.filter_by(email=email).first_or_404()

    user.email_confirmed = True

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('blog'))    
        
@app.route('/blog_post', methods=('GET', 'POST'))
@author_required
def blog_post():
    form = PostForm()
    if form.validate_on_submit():
        image = request.files.get('image')
        filename = None
        try:
            filename = uploaded_images.save(image)
        except:
            flash("The image was not uploaded")
        if form.new_category.data:
            new_category = Category(form.new_category.data)
            db.session.add(new_category)
            db.session.flush()
            category = new_category
        else:
            category = form.category.data
        blog = Blog.query.first()
        author = Author.query.filter_by(username=session['username']).first()
        title = form.title.data
        body = form.body.data
        slug = slugify(title)
        post = Post(blog, author, title, body, category, filename, slug)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog_article', slug=slug))
    return render_template('blog/blog_post.html', form=form, action="new")
    
@app.route('/blog_article/<slug>')
def blog_article(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    return render_template('blog/blog_article.html', post=post)
    
@app.route('/edit/<int:post_id>', methods=('GET', 'POST'))
@author_required
def edit(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404()
    form = PostForm(obj=post)
    if form.validate_on_submit():
        original_image = post.image
        form.populate_obj(post)
        if form.image.has_file():
            image = request.files.get('image')
            try:
                filename = uploaded_images.save(image)
            except:
                flash("The image was not uploaded")
            if filename:
                post.image = filename
        else:
            post.image = original_image
        if form.new_category.data:
            new_category = Category(form.new_category.data)
            db.session.add(new_category)
            db.session.flush()
            post.category = new_category
        db.session.commit()
        return redirect(url_for('article', slug=post.slug))
    return render_template('blog/post.html', form=form, post=post, action="edit")

@app.route('/delete/<int:post_id>')
@author_required
def delete(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404()
    post.live = False
    db.session.commit()
    flash("Article deleted")
    return redirect('/blog_admin')