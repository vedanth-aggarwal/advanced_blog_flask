from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired(message='Empty Field')])
    subtitle = StringField("Subtitle", validators=[DataRequired(message='Empty Field')])
    img_url = StringField("Blog Image URL", validators=[DataRequired(message='Empty Field'), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired(message='Empty Field')])
    submit = SubmitField("Submit Post")

class CommentForm(FlaskForm):
    body = CKEditorField("Comment", validators=[DataRequired(message='Empty Field')])
    submit = SubmitField("Submit Comment")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(message='Empty Field')])
    password = PasswordField("Password", validators=[DataRequired(message='Empty Field')])
    name = StringField("Name", validators=[DataRequired(message='Empty Field')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(message='Empty Field')])
    password = PasswordField("Password", validators=[DataRequired(message='Empty Field')])
    name = StringField("Name", validators=[DataRequired(message='Empty Field')])
    submit = SubmitField('Login')