#### Given below are the steps to run the server
- Create a virtual environment using the command
    py -m venv env   (on windows)
    python3 -m venv env   (on macOS and linux)
- Activate the virtual environment using the command
   .\env\scripts\activate   (on windows)
   source env/bin/activate (on macOS and linux)
- Install the requirements using the command
   pip install django djangorestframework
 - Perform the migration using the command
   python manage.py migrate
 - Run the server with the command
    python manage.py runserver

The API can be tested using the Browsable API or command line tools like httpie or curl
### httpie
Open up another command prompt and do the following
(pip install httpie)
#### signup
     http POST http://localhost:8000/users/ username="[username]" password="[password]"
#### Create movie
    http -a [username]:[password] http://localhost:8000/movies/ name="[name]" genre="[genre]" rating=[decimal like 8.8] date="[yyyy-mm-dd]"
#### Retrieve
     http http://localhost:8000/movies/[id]/
#### Delete
	http -a [username]:[password] DELETE http://localhost:8000/movies/[id]/
#### Update
	http -a [username]:[password] http://localhost:8000/movies/ name="[name]" genre="[genre]" rating=[decimal like 8.8] date="[yyyy-mm-dd]"
(Have to be logged in  as the creator for delete and update)
#### List of movies( with search and sort functionality)
	http http://localhost:8000/movies/?search=[searchString]&sort-by=[name or date]
	(Try the URL on the browser)
#### List of movies by user
	http http://localhost:8000/movies-by-user/?username=[username]
	or
	http http://localhost:8000/movies-by-user/?user-id=[user-id]
### Using the Browsable API
#### signup
- Go to the url http://localhost:8000/users/ 
- Fill up the form at the bottom and submit
- Login as the created user by clicking the login link at the top-right corner
#### login
- The login link is at the top-right corner of any page.
  Its url is http://localhost:8000/api-path/login/
#### Create movie
- Go to the url http://localhost:8000/movies/
- Fill up the form at the bottom and submit
#### Retrieve, update and destroy
- Go to the url http://localhost:8000/movies/[id]/
- If logged in, the delete button and the update form will be visible
#### List of movies( with search and sort functionality)
	http://localhost:8000/movies/?search=[searchString]&sort-by=[name or date]
#### List of movies by user
	http://localhost:8000/movies-by-user/?username=[username]
	or
	http http://localhost:8000/movies-by-user/?user-id=[user-id]