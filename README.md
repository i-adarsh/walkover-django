# Walkover Quiz Application

This is a full stack web application created using Django framework for back-end and html, css and JavaScript for front end. And added CI-CD pipeline through Jenkins. The main aim of this project that a registered admin can create test according to his/her needs and specifications and can view the result of each candidate. Hello

## Requirements

```bash
asgiref==3.4.1
cffi==1.14.6
crispy-bootstrap5==0.5
cryptography==3.4.8
Django==3.2.7
django-crispy-forms==1.12.0
django-environ==0.7.0
django-otp==1.1.1
gunicorn==20.1.0
mysqlclient==2.0.3
pycparser==2.20
pytz==2021.1
qrcode==7.3
sqlparse==0.4.2
uWSGI==2.0.19.1
```


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip install -r requirements.txt
```

## Working:

>1. The registered admin has to insert his email id and password, after successful email verification via OTP an admin can login into the system.
>2. After a successful login, the admin can create a custom test by choosing the topic, number of questions and time required to complete the assignment.
>
>3. After creating the test a unique link is generated which can be shared with the candidates.
>4. After completion of the test, admin can view the result of each candidate.

## Technology Used

![AWS](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)&emsp;
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)&emsp;
![Bootstrap](https://img.shields.io/badge/Bootstrap-4853D?style=for-the-badge&logo=bootstrap&logoColor=white)&emsp;
![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)&emsp;
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)&emsp;![CSS](https://img.shields.io/badge/CSS3-1572D6?style=for-the-badge&logo=css3&logoColor=white)&emsp;![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)&emsp;
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=Jenkins&logoColor=white)&emsp;


## Deployment

Application is deployed on top of AWS EC2 Instance and CI/CD pipeline is deployed through Jenkins.

| Web-page | Link | 
|   ----   | ---- |
| Live Project|[`Click here`](http://54.175.247.107/login)| 
| Admin-Login |[`Click here`](http://54.175.247.107/admin) |

## Project Setup
Steps to setup and run our project locally on your machine

>1. Install git on your machine if not installed already
>To install [`click here`](https://git-scm.com/downloads) for Windows or 
Run command `$ sudo apt-get install git` for Linux
>2. Clone the repository 
`git clone https://github.com/i-adarsh/walkover-django`
>
>3. Go inside the cloned directory on the terminal.
>4. Start virtual environment by command <br>
`virtual env`
>5. Install the required packages by command <br>
`pip install -r requirements.txt`
>
>
>6. Start the project by running `python3 manage.py runserver 0.0.0.0:8000`
>7. Open any browser and access the web application by following link    `http://localhost:8000/`

## Contributors
>[Adarsh Kumar](https://github.com/i-adaresh)
>
>[Vaibhav](https://github.com/)
>
>[Antriksh](https://github.com/Antriksh1234)

## License
[MIT](https://choosealicense.com/licenses/mit/)
