## Main Project Flask Run Page

## Import "prefix" code into your Flask app to make your app usable when running
## Flask either in the csel.io virtual machine or running on your local machine.
## The module will create an app for you to use
import prefix
import sqlite3

from flask import Flask, url_for, make_response, render_template

# create app to use in this Flask application
app = Flask(__name__)

# Insert the wrapper for handling PROXY when using csel.io virtual machine
# Calling this routine will have no effect if running on local machine
prefix.use_PrefixMiddleware(app)   

#our database
database = 'ourdata.db'

#function to get the database
def get_database():
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row # gets us access to columns by name
    return conn

# test route to show prefix settings
@app.route('/prefix_url')  
def prefix_url():
    return 'The URL for this page is {}'.format(url_for('prefix_url'))

###############################################################################
## Required Routes for Project:
##
##     1. static text page, "index"   @app.route(/)
##     2. static text page, "about"   @app.route('/about')
##     3. dynamic page, "login"       @app.route('/login')
##     4. dynamic page, "home"        @app.route('/home') - Liam
##     6. dynamic page,"recents"      @app.route('/recents') - Brady
##     7. dynamic page, "newfriends"  @app.route('/friends') - Brad
##     8. dynamiv page, "upcoming"    @app.route('/upcoming') - Quinn
##
################################################################################
@app.route('/')
def index():
    return render_template("full.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/recents')
def recents():
    return render_template("recents.html")

@app.route('/friends')
def friends():
    return render_template("friends.html")

@app.route('/upcoming')
def upcoming():
    return render_template("upcoming.html")

###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=2222)