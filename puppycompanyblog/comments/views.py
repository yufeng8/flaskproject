from flask import render_template,redirect,url_for,flash,Blueprint
from flask_login import login_required
from puppycompanyblog import db
from puppycompanyblog.models import BlogPost,Comment
from puppycompanyblog.comments.forms import AddCommentForm

comments = Blueprint("comments", __name__)

@comments.route('/post/<int:blog_post_id>/comment', methods=['GET', 'POST'])
@login_required
def comment_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    form = AddCommentForm()

    if form.validate_on_submit():
        comment = Comment(text=form.text.data, blog_post_id=blog_post_id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been posted successfully!')
        return redirect(url_for("core.index"))
    return render_template("comment_post.html", title="Comment Post", form=form)
