import urllib.request, urllib.parse
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, url_for,request,jsonify,get_flashed_messages,send_file
from flask_migrate import Migrate
import json
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField,PasswordField, SearchField
from flask_login import login_required,login_user,logout_user,current_user,UserMixin, LoginManager
from flask_marshmallow import Marshmallow
from flask import(
Flask,g,redirect,render_template,request,session,url_for,flash,jsonify
)
from flask_cors import CORS
#from flask_uploads import UploadSet,IMAGES, configure_uploads



app=Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:password@eligibility.central.edu.gh:5432/alumni'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://post:password@eligibility.central.edu.gh:5432/alumni'
app.config['SECRET_KEY'] =" thisismysecretkeykeykeykeykeyekeyekeyejyeekyejey"
app.config['UPLOADED_PHOTOS_DEST'] ='uploads'

# photos=UploadSet('photos', IMAGES)
# configure_uploads(app, photos)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)



login_manager = LoginManager(app)
login_manager.login_view = "ulogin"
login_manager.login_message_category = "info"
migrate = Migrate(app, db)

from forms import *

@login_manager.user_loader
def load_user(user_id):
    return Person.query.get(int(user_id))




def sendtelegram(params):
    url = "https://api.telegram.org/bot5738222395:AAEM5NwDAN1Zc052xI_i9-YlrVnvmSkN9p4/sendMessage?chat_id=-633441737&text=" + urllib.parse.quote(params)
    content = urllib.request.urlopen(url).read()
    print(content)
    return content

''''
#login for admin
class User:
    username = StringField('username', validators=[DataRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=80)])
    submit = SubmitField('Login')
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='admin', password='central'))
users.append(User(id=2, username='likem', password='likem'))
users.append(User(id=3, username='john', password='some'))



@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
'''

#DATABASE MODEL
#person table
class Person(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200), nullable=True)
    yearCompleted= db.Column(db.String(200), nullable=True)
    nationality= db.Column(db.String(200), nullable=True)
    contact= db.Column(db.Integer(), nullable=True)
    email= db.Column(db.String(200), nullable=True)
    faculty= db.Column(db.String(200), nullable=True)
    hallofresidence= db.Column(db.String(200), nullable=True)
    password= db.Column(db.String(20))
    school= db.Column(db.String(20))
    email= db.Column(db.String(20), nullable=True)
    phone= db.Column(db.String(10), nullable=True )
    indexnumber=db.Column(db.String())
    password=db.Column(db.String)
    gender= db.Column(db.String()    )
    department= db.Column(db.String()    )
    program= db.Column(db.String()   )
    telephone= db.Column(db.String()   )
    admitted= db.Column(db.Integer()  )
    address= db.Column(db.String()   )
    work= db.Column(db.String()  )
    guardian= db.Column(db.String()  )
    kin= db.Column(db.String()   )
    relationship= db.Column(db.String()  )
    marital= db.Column(db.String()   )
    health= db.Column(db.String()    )
    form=db.Column(db.String())
    extra= db.Column(db.String()     )
    image_file = db.Column(db.String(20))
    def __repr__(self):
        return f"Person('{self.id}', {self.name}', {self.yearCompleted})"

class alumni(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(20) )
    name= db.Column(db.String(200) )
    password= db.Column(db.String(200) )
    email= db.Column(db.String(20) )
    indexnumber= db.Column(db.String(10)  )
    telephone= db.Column(db.String(10)  )
    def __repr__(self):
        return f"alumni('{self.id}', {self.name}', {self.email})"

    
    
class Student(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    schools= db.Column(db.String()  )
    year= db.Column(db.String()  )
    fees= db.Column(db.String()  )
    arrears= db.Column(db.String()  )
    index= db.Column(db.String()  )
    guardian= db.Column(db.String()  )
    def __repr__(self):
        return f"User('{self.id}', {self.fullname}"
    
    
class User(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    arrears= db.Column(db.String()  )
    guardian= db.Column(db.String()  )
    image_file = db.Column(db.String(20))
    def __repr__(self):
        return f"User('{self.id}', {self.arrears}"
 
  
class Storypost(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    fullname= db.Column(db.String()  )
    work= db.Column(db.String()  )
    guardian= db.Column(db.String()  )
    image_file = db.Column(db.String(20))
    def __repr__(self):
        return f"User('{self.id}', {self.fullname}"
    
class Department(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String())
    school= db.Column(db.String()) 
    def __repr__(self):
        return f"Department('{self.id}', {self.name}'"
    
class School(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    def __repr__(self):
        return f"School('{self.id}', {self.name}'"
    
class Chatus(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    chatme=db.Column(db.String)
    def __repr__(self):
        return f"School('{self.id}', {self.chatme}'"
    
    
    
class Postme(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    extra=db.Column(db.String)
    address=db.Column(db.String)
    telephone=db.Column(db.String)
    def __repr__(self):
        return f"School('{self.id}', {self.extra}'"
    
        
class Year(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    def __repr__(self):
        return f"year('{self.id}', {self.name}'"
    
class Program(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String) 
    school =db.Column(db.String) 
    department =db.Column(db.String) 
    def __repr__(self):
        return f"Program('{self.id}', {self.name}'"
    
    
@app.route('/dashboard')
@login_required
def dashboard():
    if current_user == None:
        flash("Welcome to the CentralAlumina " + current_user.email, "Success")
        flash(f"There was a problem")
    return render_template('dashboard.html')

    
@app.route('/getstudent')
def getstudent():
    return render_template('getstudent.html')

@app.route('/addbill', methods=['GET', 'POST'])
@login_required
def addbill():
    print("Entering addbill function")
    form=Programfield()
    print("Form object created:", form)
    if form.validate_on_submit():
        print("Form is valid")
        school = form.school.data
        department = form.department.data
        name = form.name.data
        print("Form data:", school, department, name)
        users=Program(  
                   school=school,  
                   department=department,  
                   name=name,    
                )
        db.session.add(users)
        db.session.commit()
        print("Added new bill to database")
        flash("You just added a new bill", "success")
        return redirect('newdash')
    print("Form is not valid")
    print("Form errors:", form.errors)
    return render_template('addbill.html', form=form)

@app.route('/votes')
def votes():
    users=User.query.order_by(User.id.desc()).all()
    return render_template('votes.html', users=users)


@app.route('/list/<int:userid>', methods=['GET', 'POST'])
@login_required
def list(userid):
    form = Registration()
    print(form.indexnumber.data)

    if request.method == "POST": 
        if form.validate_on_submit():
            print('Success')
            user =Person(indexnumber=form.indexnumber.data)
            db.session.add(user)
            db.session.commit()
            return redirect('/profileid')
    print("Fetching one")
    profile=User.query.get_or_404(userid)
    print(current_user)
    user=Postme.query.order_by(Postme.id.desc()).all()
    print(user)
    return render_template("profileid.html",current_user=current_user, user=user, profile=profile, title="list",form=form)
 
 
@app.route('/user1/<int:userid>', methods=['GET', 'POST'])
@login_required
def user1(userid):
    form=Chatsingle()
    if form.validate_on_submit():
  
            new=Chatus(
                   chatme=form.chatme.data,  
                  )
            db.session.add(new)
            db.session.commit()
            return redirect('#')
    profile=User.query.get_or_404(userid)
    
    user=Chatus.query.order_by(Chatus.id.desc()).all()
    print("chatme working")
    return render_template("singleid.html",current_user=current_user, user=user, profile=profile, title="list",form=form)
 

@app.route('/addpost', methods=['GET', 'POST'])
@login_required
def addpost():
    form=Post()
    if form.validate_on_submit():
  
            post=Postme(  
                   telephone=form.telephone.data,  
                  
                   address=form.address.data,  
                   
                  extra=form.extra.data,    
               
                  )
       
            db.session.add(post)
            db.session.commit()
            flash("You Just Wrote a Post", "success")
            return redirect('/userbase')
    print(form.errors)
    return render_template("addpost.html", form=form)



@app.route('/addalumni', methods=['GET', 'POST'])
@login_required
def addalumni():
    form=Addstudent()
    if form.validate_on_submit():
  
            new=Student(schools=form.schools.data,
                   year=form.year.data,  
                   fees=form.fees.data,  
                   index=form.index.data,  
                   arrears=form.arrears.data,  
                   guardian=form.guardian.data,  
                  )
       
            db.session.add(new)
            db.session.commit()
            flash("New Student added", "success")
            return redirect('/newdash')
    print(form.errors)
    return render_template("addAlumni.html", form=form)



@app.route('/addnews', methods=['GET', 'POST'])
@login_required
def addnews():
    form=Adduser()
    if form.validate_on_submit():
  
            new=User(  
                   arrears=form.arrears.data,  
                   guardian=form.guardian.data,  
                    
               image_file=form.image_file.data
                  )
       
            db.session.add(new)
            db.session.commit()
            flash("News Added", "success")
            return redirect('/newdash')
    print(form.errors)
    return render_template("addnews.html", form=form)


@app.route('/single/<int:userid>', methods=['GET', 'POST'])
@login_required
def single(userid):
    form=Chatsingle()
    if form.validate_on_submit():
  
            new=Chatus(
                 
                  
                   chatme=form.chatme.data,  
                     
               
                  )
       
            db.session.add(new)
            db.session.commit()
            return redirect('#')
   
    print("chat try")
    user=Chatus.query.order_by(Chatus.id.desc()).all()
    return render_template("single.html",current_user=current_user, user=user, title="list",form=form)
 
 

@app.route('/addstatus', methods=['GET', 'POST'])
def addstatus():
    form=Story()
    
    if form.validate_on_submit():
            new=Storypost(fullname=form.fullname.data,
                   work=form.work.data,  
                   guardian=form.guardian.data,  
               image_file=form.image_file.data
                  )
            print('new shit')
            db.session.add(new)
            db.session.commit()
            print(new)
            flash("Thank you for sending you Prescriptions, Someone will reach out to you soon.", "success")
            return redirect('/mains')
    print(form.errors)
    return render_template("addstatus.html", form=form)


@app.route('/chats', methods=[ 'POST'])
@login_required
def chats():  
    return render_template("search.html")



@app.route('/loading')
@login_required
def loading():  
    return render_template("loading.html")


@app.route('/page')
def main():  
    return render_template("page.html")


@app.route('/')
def mains():  
    name=Person.query.order_by(Person.id.desc()).all()
    users=User.query.order_by(User.id.desc()).all()
    user=Postme.query.order_by(Postme.id.desc()).all()
    story=Storypost.query.order_by(Storypost.id.desc()).all()
    print(current_user)
    return render_template("mains.html", name=name, users=users,user=user,current_user=current_user, story=story)
 
 
@app.route('/level')
def level():  
    name=Person.query.order_by(Person.id.desc()).all()
    users=Student.query.order_by(Student.id.desc()).all()
    user=Postme.query.order_by(Postme.id.desc()).all()
    story=Storypost.query.order_by(Storypost.id.desc()).all()
    print(current_user)
    return render_template("level.html", name=name, users=users,user=user,current_user=current_user, story=story)
 
@app.route('/bill')
def bill():  
    
    name=Person.query.order_by(Person.id.desc()).all()
    bill=Program.query.order_by(Program.id.desc()).all()
    users=User.query.order_by(User.id.desc()).all()
    user=Postme.query.order_by(Postme.id.desc()).all()
    story=Storypost.query.order_by(Storypost.id.desc()).all()
    print(current_user)
    return render_template("bill.html", name=name,bill=bill, users=users,user=user,current_user=current_user, story=story)
 
 
@app.route('/news')
def news():  
    users=User.query.order_by(User.id.desc()).all()
    return render_template("news.html", users=users)
 
@app.route('/profile')
def profile():  
    name=Person.query.order_by(Person.id.desc()).all()
    users=User.query.order_by(User.id.desc()).all()
    user=Postme.query.order_by(Postme.id.desc()).all()
    story=Storypost.query.order_by(Storypost.id.desc()).all()
    print(current_user)
    return render_template("profile.html", name=name, users=users,user=user,current_user=current_user, story=story)
 

@app.route('/main1')
def main1():  
    return render_template("main1.html")


@app.route('/lofin')
def lofin():  
    return render_template("stafflogin.html")


@app.route('/newdash')
@login_required
def newdash():  
    return render_template("newdash.html")


@app.route('/search', methods=[ 'POST'])
def search():
    form= Search() # Initialize postsearched with an empty string or a suitable default value

    if request.method == 'POST': 
        posts =User.query
        if form.validate_on_submit():
            postsearched=form.searched.data
            posts =posts.filter(User.index.like('%'+ postsearched + '%') )
            posts =posts.order_by(User.index).all() 
            flash("You searched for "+ postsearched, "success")  
            print(posts)   
            print(current_user)   
    return render_template("search.html", form=form, searched = postsearched, posts=posts,current_user=current_user)





@app.route('/chatid/<int:userid>', methods=['GET', 'POST'])
@login_required
def chatid(userid):
    form = Registration()
    print(form.name.data)

    if request.method == "POST": 
        if form.validate_on_submit():
            print('Success')
            user =Person(name=form.name.data)
            db.session.add(user)
            db.session.commit()
            return redirect('#')
    print("Fetching one")
    profile=Person.query.get_or_404(userid)
    print(current_user)
    return render_template("chatid.html",current_user=current_user,  profile=profile,form=form)
 

@app.route('/story/<int:userid>', methods=['GET', 'POST'])
@login_required
def story(userid):
    form = Story()
    print(form.indexnumber.data)

    if request.method == "POST": 
        if form.validate_on_submit():
            print('Success')
            user =Storypost(indexnumber=form.indexnumber.data)
            db.session.add(user)
            db.session.commit()
            return redirect('#')
    print("Fetching one")
    profile=Storypost.query.get_or_404(userid)
    print(current_user)
    user=Postme.query.order_by(Postme.id.desc()).all()
    print(user)
    return render_template("storyid.html",current_user=current_user, user=user, profile=profile, title="list",form=form)
 




@app.route('/lists', methods=['GET', 'POST'])
@login_required
def listss():
    print("Fetching all")
    users=User.query.order_by(User.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("lists.html", users=users, current_user=current_user, title="list")


@app.route('/chatss', methods=['GET', 'POST'])
@login_required
def chatss():
    print("Fetching all")
    users=Person.query.order_by(Person.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("chatid.html", users=users, current_user=current_user, title="list")




@app.route('/<int:year>/newschools', methods=['GET', 'POST'])
def newschools(year ):
    form=Addschool()
    schools=School.query.all()
    if request.method== 'POST':
        schools=School(name=form.data)
        db.session.add(schools)
        db.session.commit()
    return render_template('newschools.html', form=form, title="newschools",schools=schools,year=year)



@app.route('/userlogout')
@login_required
def userlogout():
    if current_user:
        logout_user()
        # print(current_user.email)
    else:
        print("Well that didnt work")
    flash('You have been logged out.','danger')
    return redirect(url_for("userlanding"))








@app.route('/information')
@login_required
def information():
    persons=Person.query.order_by(Person.id.desc()).all()
    print(persons)
    return render_template("information.html", persons=persons)
 



#CRUD(update and delete routes)
@app.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id):
    form=Adduser()
    user=User.query.get_or_404(id)
    if request.method== 'GET':
        form.fullname.data = user.fullname
        form.indexnumber.data = user.indexnumber
        form.gender.data = user.gender
        form.school.data = user.school
        form.department.data = user.department
        form.completed.data = user.completed
        form.admitted.data = user.admitted
        form.email.data = user.email   
        form.telephone.data = user.telephone  
        form.hall.data = user.hall  
        form.nationality.data = user.nationality   
        form.address.data = user.address  
        form.work.data = user.work 
        form.guardian.data = user.guardian   
        form.marital.data = user.marital   
        form.extra.data = user.extra  
        form.image_file.data = user.image_file 
    if request.method== 'POST':
        new=User(fullname=form.fullname.data,
                 indexnumber=form.indexnumber.data,
                   gender=form.gender.data, 
                    school=form.school.data,
                    department=form.department.data,
                   completed=form.completed.data,
                   admitted=form.admitted.data,
                   email=form.email.data,  
                   telephone=form.telephone.data,  
                   hall=form.hall.data,  
                   nationality=form.nationality.data,  
                   address=form.address.data,  
                   work=form.work.data,   
                   guardian=form.guardian.data,  
                  marital=form.marital.data,
                  extra=form.extra.data,    
               image_file=form.image_file.data
                  )
        try:    
            db.session.add(new)
            db.session.commit()
            return redirect(url_for('list')) 
        except:
            return render_template("dashboard.html")
    return render_template("addAlumni.html", form=form)
    


   
#CRUD(update and delete routes)
@app.route("/updateuser/<int:id>", methods=['POST', 'GET'])
def updateuser(id):
    form=RegistrationForm()
    user=Person.query.get_or_404(id)
    if request.method== 'GET':
        form.name.data = user.name
        form.indexnumber.data = user.indexnumber
        form.gender.data = user.gender
        form.school.data = user.school
        form.department.data = user.department
        form.yearCompleted.data = user.yearCompleted
        form.admitted.data = user.admitted
        form.email.data = user.email   
        form.telephone.data = user.telephone  
        form.hallofresidence.data = user.hallofresidence  
        form.nationality.data = user.nationality   
        form.address.data = user.address  
        form.work.data = user.work 
        form.guardian.data = user.guardian   
        form.marital.data = user.marital   
        form.extra.data = user.extra  
        form.image_file.data = user.image_file 
    if request.method== 'POST':
        new=Person(name=form.name.data,
                 indexnumber=form.indexnumber.data,
                   gender=form.gender.data, 
                    school=form.school.data,
                    department=form.department.data,
                   yearCompleted=form.yearCompleted.data,
                   admitted=form.admitted.data,
                   email=form.email.data,  
                   telephone=form.telephone.data,  
                   hallofresidence=form.hallofresidence.data,  
                   nationality=form.nationality.data,  
                   address=form.address.data,  
                   work=form.work.data,  
                   guardian=form.guardian.data,  
                  marital=form.marital.data,
                  extra=form.extra.data,    
               image_file=form.image_file.data
                  )
        try:    
            db.session.add(new)
            db.session.commit()
            return redirect(url_for('information')) 
        except:
            return "errror"
    return render_template("userprofile.html", form=form)
    
    
#delete route
@app.route("/delete/<int:id>")
def delete(id):
    delete=User.query.get_or_404(id)
    try:
            db.session.delete(delete)
            db.session.commit()
            return redirect(url_for('list')) 
    except: 
        return "errrrrorrr"
   
   
@app.route('/usersignup', methods=['POST','GET'])
def usersignup():
    form = Registration()
    print(form.faculty.data)
    print(form.email.data)
    print(form.name.data)
    print(form.password.data)
    if request.method == "POST": 
        if form.validate_on_submit():
            print('Success')
            user =Person(password=form.password.data, email=form.email.data, faculty=form.faculty.data, name=form.name.data)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            print(current_user)
            return redirect(url_for('ulogin'))
        else:
            print(form.errors)     
    return render_template('usersignup.html', form=form)
   

@app.route('/ulogin', methods=['POST','GET'])
def ulogin():
    form = LoginForm()
    print ('try')
    print(form.email.data)
    print(form.password.data)
    
    if form.validate_on_submit():
        print("form Validated successfully")
        user = Person.query.filter_by(email = form.email.data).first()
        login_user(user)
        flash ('Welcome to your dashboard' +' ' + user.name ,'success')
        return redirect(url_for('newdash'))
    return render_template('userlogin.html', form=form)



@app.route('/userdisplay/<int:userid>', methods=['GET', 'POST'])
@login_required
def userdisplay(userid):
    profile=User.query.get_or_404(userid)
    print(current_user)
    return render_template("userdisplay.html",current_user=current_user, profile=profile, title="list")
 

@app.route('/post')
@login_required
def post():
    return render_template("post.html")
 
 
@app.route('/chatme')
@login_required
def chatme():
    return render_template("chatme.html")
 
@app.route('/item')
def item():
    return render_template("item.html")
 
 
 


@app.route('/userlanding')
@login_required
def userlanding():
    print("Fetching all")
    flash("Please login to continue.")
    users=User.query.order_by(User.id.desc()).all()
    return render_template("userlanding.html",  users=users, current_user=current_user)
 

@app.route('/userbase',methods=['GET', 'POST'])
@login_required
def userbase():
    name=Person.query.order_by(Person.id.desc()).all()
    users=User.query.order_by(User.id.desc()).all()
    user=Postme.query.order_by(Postme.id.desc()).all()
    story=Storypost.query.order_by(Storypost.id.desc()).all()
    print(current_user)
    return render_template("userbase.html", name=name, users=users,user=user,current_user=current_user, story=story)
 


@app.route('/level100', methods=['GET', 'POST'])
def level100():
    # sendtelegram("New User on Pasco Portal level 100")
    # hundred = Course.query.filter_by(level='100').all()
    return render_template('level100.html')


@app.route('/userinformation/<int:userid>', methods=['GET', 'POST'])
@login_required
def userinformation(userid):
    profile=User.query.get_or_404(userid)
    print(current_user)
    return render_template("userinformation.html",current_user=current_user, profile=profile, title="list")
 
 
 

   
#ending user



if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0', port=8000, debug=True)
    
    
