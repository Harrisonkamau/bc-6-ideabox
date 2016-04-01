
# IdeaBox

## Description


IdeaBox is a web app made using Flask.
Allows users to post their idea(s), post their comments and upvote or downvote

~~~Python
	# Posting an idea
@app.route('/add_post', methods=['GET', 'POST'])
@login_required
def add_post():
    form = RegistrationForm(request.form, PostIdea)
    if request.method == 'POST':
        post = PostIdea(title=request.form['title'], description=request.form['description'])

        db.session.add(post)

        # save the changes to the db
        db.session.commit()
    return render_template('add_post.html')
~~~


## Features

Simple to use
              