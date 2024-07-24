## Table Descriptions and Tests

### Table 1: Users
**Table Name:** Users  
**Table Description:** Stores information about the users registered in the system.

**Fields:**
- **user_id:** Unique identifier for each user.
- **username:** The name chosen by the user for login.
- **email:** The user's email address.
- **password:** The hashed password for user authentication.
- **created_at:** The date and time when the user account was created.

**Tests:**
1. **Test adding a new user:**
   - **Pre-conditions:** The user does not exist in the database.
   - **Test Steps:**
     1. Execute the SQL statement to insert a new user.
     2. Verify the user count has increased by one.
   - **Expected Result:** User is added to the database.
   - **Actual Result:** Verify user is present in the database.
   - **Status:** Pass/Fail
   - **Notes:** N/A
   - **Post-conditions:** The new user exists in the database.

### Table 2: Friends
**Table Name:** Friends  
**Table Description:** Stores relationships between users.

**Fields:**
- **friend_id:** Unique identifier for each friendship.
- **user_id:** The identifier of the user.
- **friend_user_id:** The identifier of the friend.

**Tests:**
1. **Test adding a friend:**
   - **Pre-conditions:** Both users exist in the database.
   - **Test Steps:**
     1. Execute the SQL statement to add a new friend.
     2. Verify the friends count for the user has increased by one.
   - **Expected Result:** Friendship is added to the database.
   - **Actual Result:** Verify friendship is present in the database.
   - **Status:** Pass/Fail
   - **Notes:** N/A
   - **Post-conditions:** The friendship exists in the database.

### Table 3: Reminders
**Table Name:** Reminders  
**Table Description:** Stores reminders set by users to interact with friends.

**Fields:**
- **reminder_id:** Unique identifier for each reminder.
- **user_id:** The identifier of the user who set the reminder.
- **friend_id:** The identifier of the friend.
- **reminder_date:** The date for the reminder.
- **message:** The reminder message.

**Tests:**
1. **Test adding a reminder:**
   - **Pre-conditions:** Both users and the friendship exist in the database.
   - **Test Steps:**
     1. Execute the SQL statement to add a new reminder.
     2. Verify the reminders count for the user has increased by one.
   - **Expected Result:** Reminder is added to the database.
   - **Actual Result:** Verify reminder is present in the database.
   - **Status:** Pass/Fail
   - **Notes:** N/A
   - **Post-conditions:** The reminder exists in the database.
   
### Table 4: Challenges
**Table Name:** Challenges   
**Table Description:** Stores the weekly challenges, while inheriting from the Users, and friends tables 

**Fields:**
- **Challenge_id:** Unique identifier for each challenge.
- **title:** The name for each challenge.
- **description:** A description for each challenge.
- **joint_flag:** Boolean flag that determines if challenge is joint or individual.
- **user_ID_a:** Stores one of the users in a joint challenge foreign key to users.
- **user_ID_b:** Stores the second user in a joint challenge foreign key to users.
- **start_date:** Stores the date that the challenge begins.
- **end_date:** Stores the date that the challenge ends.


**Tests:**
1. **Test adding a new challenge:**
   - **Pre-conditions:** The challenge does not exist in the database.
   - **Test Steps:**
     1. Execute the SQL statement to insert a new challenge.
     2. Verify the challenge count has increased by one.
   - **Expected Result:** challenge is added to the database.
   - **Actual Result:** Verify challenge is present in the database.
   - **Status:** Pass/Fail
   - **Notes:** N/A
   - **Post-conditions:** The new challenge exists in the database.


## Data Access Methods and Tests

### Access Method 1: getUserById
**Name:** getUserById  
**Description:** Retrieves user information based on the user ID.

**Parameters:**
- **user_id:** The unique identifier of the user.

**Return Values:**
- **User:** The user object containing user details.

**Tests:**
1. **Test retrieving user by ID:**
   - **Pre-conditions:** The user exists in the database.
   - **Test Steps:**
     1. Execute the function with a valid user ID.
     2. Verify the returned user details match the expected user.
   - **Expected Result:** Correct user details are returned.
   - **Actual Result:** Verify the returned details.
   - **Status:** Pass/Fail
   - **Notes:** N/A
   - **Post-conditions:** User details are retrieved successfully.

### Access Method 2: getFriendsByUserId
**Name:** getFriendsByUserId  
**Description:** Retrieves friends of a user based on the user ID.

**Parameters:**
- **user_id:** The unique identifier of the user.

**Return Values:**
- **List of Friends:** The list of friends associated with the user.

**Tests:**
1. **Test retrieving friends by user ID:**
   - **Pre-conditions:** The user and friends exist in the database.
   - **Test Steps:**
     1. Execute the function with a valid user ID.
     2. Verify the returned list of friends matches the expected list.
   - **Expected Result:** Correct list of friends is returned.
   - **Actual Result:** Verify the returned list.
   - **Status:** Pass/Fail
   - **Notes:** N/A
   - **Post-conditions:** List of friends is retrieved successfully.

### Access Method 3: getRemindersByUserId
**Name:** getRemindersByUserId  
**Description:** Retrieves reminders for a user based on the user ID.

**Parameters:**
- **user_id:** The unique identifier of the user.

**Return Values:**
- **List of Reminders:** The list of reminders associated with the user.

**Tests:**
1. **Test retrieving reminders by user ID:**
   - **Pre-conditions:** The user and reminders exist in the database.
   - **Test Steps:**
     1. Execute the function with a valid user ID.
     2. Verify the returned list of reminders matches the expected list.
   - **Expected Result:** Correct list of reminders is returned.
   - **Actual Result:** Verify the returned list.
   - **Status:** Pass/Fail
   - **Notes:** N/A
   - **Post-conditions:** List of reminders is retrieved successfully.