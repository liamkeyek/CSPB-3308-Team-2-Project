## Main Project Flask Run Page

## Import "prefix" code into your Flask app to make your app usable when running
## Flask either in the csel.io virtual machine or running on your local machine.
## The module will create an app for you to use
import prefix
import sqlite3
from flask import Flask, request, url_for, make_response, render_template, jsonify, redirect
from datetime import datetime, timedelta
import calendar

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
##     6. dynamic page, "recents"     @app.route('/recents') - Brady
##     7. dynamic page, "newfriends"  @app.route('/friends') - Brad
##     8. dynamic page, "upcoming"    @pp.route('/upcoming') - Brady   
##     9. dynamiv page, "challenges"  @app.route('/challenges') - Quinn
##     10. endpoint, "accept_challenge" @app.route('/accept_challenges') - Quinn
##
################################################################################
@app.route('/')
def index():
    return render_template("full.html")

"""
Home Route ('/home'):
Displays a monthly calendar view with reminders.
Features:
- Shows a monthly calendar
- Allows navigation between months
- Highlights the current day
- Displays reminders for specific dates
Query Parameters:
- month (int): The month to display (1-12)
- year (int): The year to display
Notes:
- Handles year rollover when navigating between months
- Uses the 'calendar' module to generate calendar data
- Currently uses hardcoded reminder data

Last updated: Liam Keyek (8/5/2024)
"""
@app.route('/home')
def home():
    current_date = datetime.now()
    month = request.args.get('month', default=current_date.month, type=int)
    year = request.args.get('year', default=current_date.year, type=int)

    # Ensure month is within 1-12
    if month < 1:
        month, year = 12, year - 1
    elif month > 12:
        month, year = 1, year + 1

    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]

    prev_month = month - 1 if month > 1 else 12
    prev_year = year if month > 1 else year - 1
    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1

    # Updated reminders data
    reminders = {
        15: ["Call Liam", "Call Brad"],
        22: ["Call Brady"],
        28: ["Call Quinn"]
    }

    current_day = current_date.day if current_date.month == month and current_date.year == year else None

    return render_template("home.html", 
                           cal=cal,
                           month_name=month_name,
                           year=year,
                           reminders=reminders,
                           prev_month=prev_month,
                           prev_year=prev_year,
                           next_month=next_month,
                           next_year=next_year,
                           current_day=current_day)

"""
Add Reminder Route ('/add_reminder'):
Placeholder for adding new reminders to the calendar.
Features:
- Currently renders a template for adding reminders

Last updated: Liam Keyek (8/5/2024)
"""
@app.route('/add_reminder')
def add_reminder():
    # Render a template for adding reminders (create add_reminder.html in templates folder)
    return render_template("add_reminder.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/recents')
def recents():
    conn = get_database()
    c = conn.cursor()
    user_id = 1  # change for each specific user
    c.execute('''
        SELECT R.reminder_id, U.username, R.last_messaged, R.reminder_date, R.message, F.relationship_type
        FROM Reminders R
        JOIN Friends F ON R.friend_id = F.friend_id
        JOIN Users U ON F.friend_user_id = U.user_id
        WHERE R.user_id = ?
    ''', (user_id,))
    reminders = c.fetchall()
    conn.close()
    return render_template("recents.html", reminders=reminders)

@app.route('/friends')
def friends():
    return render_template("friends.html")

@app.route('/add_friend', methods=['POST'])
def add_friend():
    # Check if request has JSON data or is a form submission
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    print("Received data: ", data)  # Debugging statement
    user_id = data.get('user_id')
    friend_user_id = data.get('friend_user_id')
    relationship_type = data.get('relationship_type')
    print(
        f"user_id: {user_id}, friend_user_id: {friend_user_id}, relationship_type: {relationship_type}"
    )  # Debugging statement
    # Validate inputs
    if not all([user_id, friend_user_id, relationship_type]):
        response = {'message': 'Invalid input'}
        return jsonify(response), 400
    # Connect to your database
    conn = sqlite3.connect('ourdata.db')
    cursor = conn.cursor()
    # Insert the new friend into the database
    cursor.execute(
        '''
        INSERT INTO friends (user_id, friend_user_id, relationship_type)
        VALUES (?, ?, ?)
    ''', (user_id, friend_user_id, relationship_type))
    conn.commit()
    conn.close()
    response = {'message': 'Friend added successfully!'}
    if request.is_json:
        return jsonify(response)
    else:
        return redirect(url_for('display_friends'))

@app.route('/display_friends')
def display_friends():
    conn = get_database()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT user_id, friend_user_id, relationship_type FROM friends')
    friends = cursor.fetchall()
    conn.close()
    return render_template('display_friends.html', friends=friends)

@app.route('/upcoming')
def upcoming():
    return render_template("upcoming.html")

@app.route('/challenges')
def challenges():
    conn = get_database()
    c = conn.cursor()
    user_id = 1
    c.execute('''
        SELECT challenge_id, title, description, joint_flag, user_id_a, user_id_b, start_date, end_date
        FROM Challenges
        WHERE user_id_a = ? OR user_id_b = ?
    ''', (user_id, user_id))
    challenges = c.fetchall()
    conn.close()
    
    formatted_challenges = []
    for challenge in challenges:
        formatted_challenge = {
            'challenge_id': challenge[0],
            'title': challenge[1],
            'description': challenge[2],
            'joint_flag': challenge[3],
            'user_id_a': challenge[4],
            'user_id_b': challenge[5],
            'start_date': challenge[6],
            'end_date': challenge[7],
            'status': 'Active' if datetime.strptime(challenge[6], '%Y-%m-%d').date() <= datetime.now().date() <= datetime.strptime(challenge[7], '%Y-%m-%d').date() else 'Expired'
        }
        formatted_challenges.append(formatted_challenge)

    return render_template("challenges.html", challenges=formatted_challenges)

@app.route('/accept_challenge', methods=['POST'])
def accept_challenge():
    data = request.json
    challenge_id = data.get('challenge_id')
    user_id = 1  

    conn = get_database()
    c = conn.cursor()


    c.execute('''
        SELECT * FROM Challenges
        WHERE challenge_id = ? AND (user_id_a = ? OR user_id_b = ?)
    ''', (challenge_id, user_id, user_id))
    challenge = c.fetchone()

    if challenge:
        conn.close()
        return jsonify({'message': 'Challenge accepted successfully!'})
    else:
        conn.close()
        return jsonify({'message': 'Challenge not found or you are not part of this challenge.'}), 404

    

###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=2222)