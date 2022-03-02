from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class AddStud(FlaskForm):
    first_name = StringField("Student first Name", validators = [DataRequired()])
    surname = StringField("Student Surname",validators = [DataRequired()])
    house_num = IntegerField("Student Home Number", validators = [DataRequired()])
    postcode = StringField("Student Postcode", validators = [DataRequired()])
    submit = SubmitField ("Add Item")

class AddClass(FlaskForm):
    name = StringField("Class Name",validators = [DataRequired()])
    desc = StringField("Class Description",validators = [DataRequired()])
    submit = SubmitField ("Add Item")

class AddEnrollment(FlaskForm):
    fk_student = SelectField("Student Name", choices=[] , validators = [DataRequired()])
    fk_class = SelectField("Class to enroll", choices=[] , validators = [DataRequired()])
    submit = SubmitField ("Add Item")
