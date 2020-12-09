from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length

class LoginForm(FlaskForm):
    name=StringField(label='name', validators=[DataRequired("User Name can't be empty"),Length(min=4,max=20)])
    password=PasswordField(label='password',validators=[DataRequired("Password can't be Empty!!!")])
    submit=SubmitField(label='Submit')

app=Flask(__name__)
app.config['SECRET_KEY']='kennysoft'

@app.route('/',methods=['GET','POST'])
def index():
    form=LoginForm()
    data={}
    if form.validate_on_submit():
     data['name'] =form.name.data
     data['password'] =form.password.data
    return  render_template('login.html',form=form,data=data)
if __name__=='__main__':
    app.run(debug=True)