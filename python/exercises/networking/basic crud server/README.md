# School Students managment API (Basic CRUD server)

### Description
A CRUD server for viewing and editing a student database.
JWT is implemented for authentication and authorization


Using the API you can:
* get all students
* get specific student
* add student
* get all students in a class

## Quick start
Install dependencies
```bash
pip install -r requirements.txt
```
Run the server using `uvicorn`
```bash
uvicorn server:app --reload
```

## Authentication
It's basically checking that the user is indead the person they claim they are.
This is done by checking the provided credintials (username/password) against what we have in our database.
Of course the password would be stored in an encrypted form using encryption tools like bcrypt.


## Authorization
### For authorization we will use **JWT**
A tool used to help us with authorization AFTER the user has already signed-in and authenticated.
JWT would "sign" a piece of information about the user (such as their roles) and generate a token accordingly.
Then the user would keep using that same token while they communicate with our API or service.
So, when JWT is used, the user does not have to keep providing their username and password with every request.
AKA we get Single Sign On feature!