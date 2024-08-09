# FINAL REPORT

## Project Title: Friend Nudge

## Team Members

- **Liam Keyek**
   - GitHub: [@liamkeyek](https://github.com/liamkeyek)
   - Email: like4684@colorado.edu
- **Quinn Ridgeway**
   - GitHub: [@QR199](https://github.com/QR199)
   - Email: quri8255@colorado.edu
- **Brad Richardson**
   - GitHub: [@brichardson2468](https://github.com/brichardson2468)
   - Email: brri6685@colorado.edu
- **Brady Gagerman**
   - GitHub: [@bradygagerman](https://github.com/bradygagerman)
   - Email: brga1958@colorado.edu

## Project Links

- **Project Tracker:** [Trello Board](https://trello.com/b/FuSwL9kK/cspb-3308-team-2)
- **Version Control Repository:** [GitHub Repository](https://github.com/liamkeyek/CSPB-3308-Team-2-Project)
- **Demo Video:** [Insert link when completed]
- **Public Hosting Site:** [Insert link when completed]

## What We Completed

### Liam
For this project, I took on the task of creating the calendar page, which ultimately became our home page. I implemented a functional monthly calendar view using Flask for the backend and HTML/CSS for the frontend. The page features a clean, responsive design with a modern color scheme, emphasizing usability and aesthetics. I developed navigation controls that allow users to move between months, handling year rollovers correctly. The calendar highlights the current day and displays reminders for specific dates, although currently, these reminders are hardcoded. I also added a header with navigation links to other parts of the application, setting up the structure for future development.

### Brad
[Insert Brad's contribution]

### Brady
[Insert Brady's contribution]

### Quinn
My primary focus during this project was to design and implement the challenges page. For the frontend development I used HTML and CSS in the same style as the other pages. My page has two flask routes, one to display the html of the challenges page and one to make the 'accept challenge' button functional. The challenges page inherits from an SQL database of challenges that contains user information, and a joint flag to determine if the instance of the challenge involves multiple users. I also have a javascript function that updates the UI for the button. The challenges page also dynamically shows the current active challenges in the database. My page is also reachable via the header menu.    

## What We Were in the Middle of Implementing

### Liam
I didn't implement the login page and unique user creation because it turned out to be way more complex than I initially thought. When we started the project, I didn't realize how much work goes into user authentication and security. It's not just about making a page where people type in a username and password; there's a whole bunch of stuff behind the scenes to keep user data safe and make sure the right person is logging in. Plus, we would have needed to set up a proper database to store user information securely, which is a big task on its own. We were also running short on time, and since the calendar was our main focus, we decided to prioritize that instead.

### Brad
[Insert Brad's in-progress work]

### Brady
[Insert Brady's in-progress work]

### Quinn
While developing the 'accept challenge' button functionality I encountered more complexity than I intially anticipated. Making this feature fully functional would require more work. Additionally making sure the databases interact correctly to handle specific challenges for specific users was another hurdle. I was researching dynamic endpoints more in an attempt to make sure challenges could be accepted by the user. This feature could use more refinement.   

## What We Had Planned for the Future

### Liam
In the future, if I wanted to add login functionality, I'd start by learning more about user authentication in Flask. I'd probably use Flask-Login, which is a library that helps manage user sessions. For the database, I'd look into using SQLAlchemy with Flask to handle user data. I'd also need to learn about password hashing to store passwords safely. To create the actual login page, I'd use HTML forms and some JavaScript for client-side validation. It would take some time to figure all this out, but it would be a cool addition to our project. I'd also make sure to include features like password reset and new account creation to make it more user-friendly.

### Brad
[Insert Brad's future plans]

### Brady
[Insert Brady's future plans]

### Quinn
I was thinking about adding a feature where the user could create a unique challenge and send it to one of their friends. The HTML and CSS for this task would probably not be super complicated. I could make a 'create challenge' button that displays the relavent forms to create the challenge. However I think I would need an additional function to add private challenges to the database, and I would probably have to put a privacy flag in the database. A privacy flag in the users datbase would also be an important feature to determine if a users profile is public or private.  

## Known Problems (Bugs, Issues)

### Liam
I do not know of any existing bugs with the current implementation of the home page.

### Brad
[Insert Brad's known issues]

### Brady
[Insert Brady's known issues]

### Quinn
As discussed in the presentation it would be wise to add privacy features for specific users. Additionally adding a mechanism to check that a specific user ID exists would be advantageous for the proposed 'create challenge' feature. 
