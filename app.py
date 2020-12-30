from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Development
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Development)
db = SQLAlchemy(app)
migrate = Migrate(app , db)



from mode_admin import admin
from mode_users import users

app.register_blueprint(admin)
app.register_blueprint(users)




#  git init
#  git remote add origin address github
#  pip3 freeze > requirements.txt
#  git config --global user.email "mansourosmani4050mnr@gmail.com"
#  git config --global user.name "Unknown-21-m"
#  git commit -m "Initialize Project"
#  git push --set-upstream origin master
# git push --set-upstream origin main
#  git push

    #  git remote remove origin


# to add a file and update
# git add filename
# git commit -m "Update filename"
# git push


# after change files we save files like these:
# git add .gitignore
# git commit - m "Update .gitignore"
# git add mode_admin
# git commit -m "Initialize admin Blueprint"
# git add app.py
# git commit -m "Register admin Blueprint to the main app"
# git push
