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