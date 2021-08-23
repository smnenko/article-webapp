# Article Web App (article-webapp) 
ArticleWA is a full-stack web application that allows read, write, edit and delete
articles. It is implement Django and djangorestframework, use JWT Token (SimpleJWT) for registration and authorization.
That project is an attempt to partially copy site medium.com, but many finctions was simplified and improved.

### Stack of Technologies
##### Backend
- Python 3.9
- Django 3.2.5
- djangorestframework 3.12.4
- PostgreSQL 13.3
##### Frontend
- Vue.js 2.6.11
- axios 0.21.1
- Bootstrap 5.0.1

### Installation
> The project requires an installed Python 3.9
- Clone git repository
```
git clone https://github.com/smnenko/article-webapp.git
```
- Create empty djngo application and copy SECRET_KEY from your_project.settings.py
- Fill all fields in /backend/.env (you sholud create new PostgreSQL database)
- Initialize virtual environment (good practice) and leave it without it
- Install all requirements that project needed (you should be in backend folder)
> If you have been installed Python2 use pip3
```
pip install -r requirements.txt
```
- Apply migrations
> Use python3 on Linux and MacOS
```
python manage.py migrate
```
- Install fixtures
```
python manage.py loaddata initial.json
```
- Install Vue.js dependencies (you should be in frontend)
```
npm install
```
- Go to frontend folder, create ".env.local" file, insert next line and save it (or replace to your host and port)
```
VUE_APP_SERVER_HOST=http://localhost:8000/api/v1/
```
- Open 2 terminals and run client and server
> You should be in backend directory for executing first command  
> You should be in frontend directory for executing second command
```
python manage.py runserver
npm start
```
- Go to http://localhost:8080/

### Screenshots
- Main page
![Main](https://github.com/smnenko/article-webapp/blob/master/docs/main.PNG)
![Main2nd](https://github.com/smnenko/article-webapp/blob/master/docs/main2dpart.PNG)
- Login page
![Login](https://github.com/smnenko/article-webapp/blob/master/docs/login.PNG)
- Registration page
![Register](https://github.com/smnenko/article-webapp/blob/master/docs/register.PNG)
- Profile page
![Profile](https://github.com/smnenko/article-webapp/blob/master/docs/profile.PNG)
- Write article page
![Write](https://github.com/smnenko/article-webapp/blob/master/docs/write.PNG)
- Read article page
![Read](https://github.com/smnenko/article-webapp/blob/master/docs/read.PNG)
- Edit article page
![Edit](https://github.com/smnenko/article-webapp/blob/master/docs/edit.PNG)
