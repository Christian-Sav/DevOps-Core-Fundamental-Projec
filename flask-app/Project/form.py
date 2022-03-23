from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from Project.models import Classes

class NameCheck():
    def __init__(self, message = "Class already exists"):
        self.message = message
    
    def __call__(self, form, field):
        if field.data in [classes.c_name for classes in Classes.query.all()]:
            raise(ValidationError(self.message))


class AddStud(FlaskForm):
    first_name = StringField("Student First Name", validators = [DataRequired()])
    surname = StringField("Student Surname",validators = [DataRequired()])
    house_num = IntegerField("Student Home Number", validators = [DataRequired()])
    postcode = StringField("Student Postcode", validators = [DataRequired()])
    submit = SubmitField ("Add Item")

class AddClass(FlaskForm):
    c_name = StringField("Class Name",validators = [DataRequired(), NameCheck()])
    c_desc = StringField("Class Description",validators = [DataRequired()])
    submit = SubmitField ("Add Item")

class AddEnrollment(FlaskForm):
    fk_student = SelectField("Student Name", choices=[] , validators = [DataRequired()])
    fk_class = SelectField("Class to enroll", choices=[] , validators = [DataRequired()])
    submit = SubmitField ("Add Item")
