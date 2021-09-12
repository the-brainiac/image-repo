# Image Gallery
## 🔧 Technology used:
### Front-End
![](https://img.shields.io/badge/html%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white)
![](https://img.shields.io/badge/css%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white)
![](https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![](https://img.shields.io/badge/jquery%20-%231572B6.svg?&style=for-the-badge&logo=jquery&logoColor=white)

### Back-End
![](https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO_rest_framework-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![](https://img.shields.io/badge/sqlite-%2307405e.svg?&style=for-the-badge&logo=sqlite&logoColor=white)

### Server
![](https://img.shields.io/badge/python_anywhere%20-%231572B6.svg?&style=for-the-badge)  

<!-- refer to this link for all badges -->
<!-- https://github.com/Ileriayo/markdown-badges -->
## [Live Demo](https://shivprojects.pythonanywhere.com/image-gallery/)
https://shivprojects.pythonanywhere.com/image-gallery/

## Source Code
[GitHub Repo link](https://github.com/the-brainiac/image-repo)  
https://github.com/the-brainiac/image-repo  

## Description

### This web app handles these Models(Tables)-  
- `Admin`
- `User`
- `Image`
- `Catagory`

> CRUD -- `Creation Retrieval Updation Deletion`
## Steps to Test it on local:
### Step - 1
Install latest version of python from https://www.python.org/downloads/
### Step - 2
Open your terminal (or powershell if you are using windows operating system.) then to clone this repo use this command -
```
git clone https://github.com/the-brainiac/image-repo.git
```
or download as zip file then extract it.
### Step - 3 (Optional)
install virtual enviornment 
```
py -m pip install --user virtualenv     #installing virtual enviornment
py -m venv env          #creating new virtual enviornment
.\env\Scripts\activate      #to activate the enviornment
````
### Step - 4
Install all required libraries and modules.
```
pip install -r requirements.txt
```

### Step - 5
move to the directory where `manage.py` file is saved (use `cd` command to change directory) and make migrations to database.
```
python manage.py makemigrations
python manage.py migrate
```
### Step - 6
Run Local server
```
python manage.py runserver
```
### Step - 7
Now open your browser and enter the url http://127.0.0.1:8000/ or http://localhost:8000/ in your browser and enjoy the app.



> If your find any problem in running the app then contact me at shiv71290@gmail.com