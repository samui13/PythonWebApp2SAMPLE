$virtualenv venv --distribute
$source venv/bin/activate
$pip install webapp2 webob jinja2 gunicorn
$foreman start
$ pip freeze > requirements.txt
.gitignore > 
venv
*.pyc
$git init
$git add .
$git commit -m "Init"
$heroku create
git push heroku master
http://powerful-falls-3944.herokuapp.com/