"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
from app import app,forms, db
import os
from flask_mail import Message
from .forms import Form
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for, flash
from app.models import UserProfile
import datetime

# app.config['SECRET_KEY'] = "prettydolphin"

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/profile',methods=['POST', 'GET'])
def upload():
    # form = ContactForm()
    # if form.validate_on_submit():
    #     msg = Message(request.form['subject'], sender=(request.form['name'],
    #     request.form['email']),recipients=["bradleythompsonbct@gmail.com"])
    #     msg.body = request.form['message']
    #     mail.send(msg)
    #     flash('Message sent from %s'%(request.form['name']))
    #     return redirect('/')
    form = Form()

    # Validate file upload on submit
    if request.method == 'POST':
        if form.validate_on_submit()==True:
            
        # Get file data and save to your uploads folder
            # # upload=form.upload.data
            # filename=secure_filename(upload.filename)
            # upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fname = form.fname.data
            lname = form.lname.data
            gender= form.gender.data
            email = form.email.data
            location = form.location.data
            bio = form.biography.data
            date = format_date_joined()
            filename = assignPath(form.upload.data)
            
            user = UserProfile(fname,lname,gender,email,location,bio,date,filename)
            db.session.add(user)
            db.session.commit()

            # remember to flash a message to the user
            flash('User information submitted successfully.')
        else:
            flash('User information not submitted')
        return redirect(url_for("upload"))  # they should be redirected to a secure-page route instead
    return render_template("profile.html", form=form)
    
@app.route("/profiles")
def profiles():
    user_profiles = db.session.query(UserProfile).all()
    return render_template("profiles.html", users=user_profiles)
    
@app.route("/profile/<userid>")
def profileId(userid):
    user = db.session.query(UserProfile).filter_by(id=int(userid)).first()
    return render_template("display.html", user=user)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

def format_date_joined():
    now = datetime.datetime.now() #current date
    ## Format the date to return only month and year date
    return now.strftime("%B %d, %Y")
    
def assignPath(upload):
    filename = secure_filename(upload.filename)
    upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return filename 

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
