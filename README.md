# Friends service
### Service for friends around the world
The goal of the project is to give people the opportunity to create online communications
### Stack:
- Python
- Django
- Git
- DRF
- Docker

### Screenshot
![Screenshot](https://github.com/neenael/friends_service/blob/main/screenshot.png)
## Endpoints
- [Get started](#get-started)
  - [Docker](#docker)
  - [Common installation](#common-installation)
- [Model description](#model-description)
- [API Documentation](#api-documentation)
  - [Friendship API](#friendship-api)
  - [FriendshipRequest API](#friendship-request-api)


## Get started

### Docker
This project contains a template Dockerfile for running Django applications in a Docker container.\
To use Docker in a Django project, you need to have Docker installed on your machine. You can download Docker Desktop on the official website\
Docker: https://www.docker.com/products/docker-desktop
1. Сopy the project from the repository:
```
$ git clone https://github.com/neenael/friends_service.git
```
2. Follow the project directory
```commandline
$ cd friends_service 
```
3. Run the command below to pull Image from DockerHub
```commandline
$ docker pull neenael/friendsserviceimage
```
4. Run the command below to run sercive
```commandline
$ docker run -p 8000:8000 --name friendsservice neenael/friendsserviceimage
```
5. [Follow the localhost (127.0.0.1:8000)](http://127.0.0.1:8000)

### Common installation
1. Сopy the project from the repository:
```
$ git clone https://github.com/neenael/friends_service.git
```
2. Set up a virtual environment
```commandline
$ python -m venv venv
```
(Skip if alreadt exists)
```commandline
$ source venv/bin/activate
```
3. Install the requirements
```commandline
$ pip install django
```
```commandline
$ pip install djangorestframework
```
```commandline
$ pip install drf-spectacular
```
Also check your GNU gettext. Update if it's necessary\
4. Follow the project directory
```commandline
$ cd friends_service 
```
5. Run migrations compilation
```commandline
$ python manage.py migrate
```
6. Execute the command to run local server
```commandline
$ python manage.py runserver
```
7. [Follow the localhost (127.0.0.1:8000)](http://127.0.0.1:8000)
## Model description
### User
The default User model represents a user in the system.

| Field                                            | Type                                    | Description                      |
|--------------------------------------------------|-----------------------------------------|----------------------------------|
| id	                                              | integer	                                | The unique ID of the user.       |
| username                                         | 	string	                                | The username of the user.        |
| email	| string	                                 | The email address of the user.   |
 | first_name	| string	                                 | The first name of the user.      |
 | last_name	| string	                                 | The last name of the user.       |
 | password	| string	| The hashed password of the user. |

### Friendship
The Friendship model represents a friendship between two members in the system.

| Field           | Type            | Description                  |
|-----------------|-----------------|------------------------------|
| member_1 | ForignKey(User) | One member of friendship     |
| member_2 | ForignKey(User)  | Another member of Friendship |

### FriendshipRequest
The FriendshipRequest model represents a friendship request from one user to another in the system.

| Field           | Type         | Description                        |
|-----------------|--------------|------------------------------------|
| request_from | ForignKey(User) | Sender of request                  |
| request_to | ForignKey(User) | Receiver of request                |
| is_received | BooleanField | If request is accepted by receiver |
## API Documentation
### /api/v1/
The api map for all models in the project is located at this address
Example:
```
{
    "friendship": "http://127.0.0.1:8000/api/v1/friendship/?format=json",
    "friendship_request": "http://127.0.0.1:8000/api/v1/friendship_request/?format=json"
}
```
### /api/v1/schema/swagger/
The OpenAPI (swagger) specification is located at this address. The specification works on the basis of the DRF Spectacular package
### /api/v1/schema/redoc/
The OpenAPI redoc specification is located at this address. The specification works the same way based on Spectacular

## Friendship API
### GET /api/v1/friendship/
Returns list of friendships.\
Response 200:
```commandline
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "date_created": "2023-05-07T17:51:26.374Z",
      "member_1": 0,
      "member_2": 0
    }
  ]
}
```
### POST /api/v1/friendship/
Creates new friendship.\
Request body:
```commandline
{
  "member_1": 0,
  "member_2": 0
}
```
Response 200:
```commandline
{
  "id": 0,
  "date_created": "2023-05-07T17:57:10.868Z",
  "member_1": 0,
  "member_2": 0
}
```
### GET /api/v1/friendship/{id}/
Retrieves friendship
Response 200:
```commandline
{
  "id": 0,
  "date_created": "2023-05-07T17:54:45.281Z",
  "member_1": 0,
  "member_2": 0
}
```



### PUT /api/v1/friendship/{id}/
Updates friendship

Request body:
```commandline
{
  "id": 0,
  "date_created": "2023-05-07T17:56:30.194Z",
  "member_1": 0,
  "member_2": 0
}
```
Response 200:
```commandline
{
  "member_1": 0,
  "member_2": 0
}
```
### PATCH /api/v1/friendship/{id}/
Patchs friendship

Request body (Example):
```commandline
{
  "member_1": 0,
  "member_2": 0
}
```
Response 200:
```commandline
{
  "id": 0,
  "date_created": "2023-05-07T17:58:01.099Z",
  "member_1": 0,
  "member_2": 0
}
```
### DELETE /api/v1/friendship/{id}/
Removes friendship

Response 200:
```commandline
{
  "id": 0,
  "date_created": "2023-05-07T17:58:58.901Z",
  "member_1": 0,
  "member_2": 0
}
```
## Friendship request API
### GET /api/v1/friendship_request/
Returns list of friendships request.\
Response 200:
```commandline
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "date_created": "2023-05-07T18:02:37.383Z",
      "member_1": 0,
      "member_2": 0
    }
  ]
}
```
### POST /api/v1/friendship_request/
Creates new friendship request.\
Request body:
```commandline
{
  "is_received": false,
  "request_from": 0,
  "request_to": 0
}
```
Response 200:
```commandline
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "date_created": "2023-05-07T18:02:37.383Z",
      "member_1": 0,
      "member_2": 0
    }
  ]
}
```
### GET /api/v1/friendship_request/{id}/
Retrives friendship request.\
Response 200:
```commandline
{
  "id": 0,
  "date_created": "2023-05-07T18:04:25.463Z",
  "member_1": 0,
  "member_2": 0
}
```
### PUT /api/v1/friendship_request/{id}
Updates friendship request.\
Request body:
```commandline
{
  "is_received": true,
  "request_from": 0,
  "request_to": 0
}
```
Response 200:
```commandline
{
  "id": 0,
  "date_created": "2023-05-07T18:05:34.230Z",
  "member_1": 0,
  "member_2": 0
}
```
### PATCH /api/v1/friendship_request/{id}
Patchs friendship request.\
Request body:
```commandline
{
  "is_received": true,
  "request_from": 0,
  "request_to": 0
}
```
Response 200:
```commandline
{
  "id": 0,
  "date_created": "2023-05-07T18:06:03.381Z",
  "member_1": 0,
  "member_2": 0
}
```
### DELETE /api/v1/friendship_request/{id}
Removes friendship request.\
Response 200:
```commandline
{
  "id": 0,
  "date_created": "2023-05-07T18:07:24.417Z",
  "member_1": 0,
  "member_2": 0
}
```
