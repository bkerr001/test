from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
## from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(Length(min=2, max=20))]
                           )
    email = StringField('Email',
                           validators=[DataRequired(), Email()]
                           )
    password = PasswordField('Password',
                        validators=[DataRequired()]
                        )
    confirm_password= PasswordField('Confirm Password',
                             validators=[DataRequired(), EqualTo('password')]
                             )
    first_name = StringField('First Name',
                           validators=[DataRequired(Length(min=2, max=20))]
                           )

    last_name = StringField('Last Name',
                           validators=[DataRequired(Length(min=2, max=20))]
                           )
    submit = SubmitField ('Create Account')




class LoginForm(FlaskForm):

    email = StringField('Email',
                           validators=[DataRequired(), Email()]
                           )
    password = PasswordField('Password',
                        validators=[DataRequired()]
                        )
    remember = BooleanField("Remember Me")

    submit = SubmitField ('Login')