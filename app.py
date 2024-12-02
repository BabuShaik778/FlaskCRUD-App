from flask  import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db=SQLAlchemy(app)

# row database
class Task(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(250),nullable=False)
    created=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) ->str:
        return  f"Task {self.id}"


with app.app_context():
    db.create_all()



#home page
@app.route("/",methods=["POST","GET"])
def index():
    if request.method =="POST":
        task_content = request.form['content']
        if not task_content.strip():
            return " task content be empty"
        new_task = Task(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
        
            return f"ERRor:{e}"
    else:
        tasks=Task.query.order_by(Task.created).all()
        return render_template('index.html',tasks=tasks)


#Delete item
@app.route("/delete/<int:id>") 
def delete (id):
    delete_task=Task.query.get_or_404(id)
    try:
        db.session. delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"ERROR:{e}"



#Edit item
@app.route("/edit/<int:id>" , methods=["GET", "POST"])
def edit(id):
    task = Task.query.get_or_404(id)
    if  request.method =="POST":
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Error:{e}"
    else:
        return render_template('edit.html',task = task)

       
if __name__== "__main__":

    app.run(debug=True)

