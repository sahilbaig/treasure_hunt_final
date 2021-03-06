from treasure import db ,login_manager
from flask_login import LoginManager,UserMixin,login_user,current_user,logout_user
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100),nullable=False,unique=True) 
    password=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False, unique=True)
    score=db.Column(db.Integer,default=0)
    time_now=db.Column(db.DateTime, nullable=False ,default=datetime.utcnow )

    def __repr__(self):
        return f"User('{self.username},{self.score}')" 

class Questions(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    quest=db.Column(db.Text, nullable=False)
    answer=db.Column(db.Text , nullable=False)
    
    def __repr__(self):
        return f"Questions('{self.quest},{self.answer}')" 
