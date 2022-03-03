from flask import redirect, url_for, render_template, request
from Project import app, db
from Project.form import AddClass, AddStud, AddEnrollment, DelClass
from Project.models import Enrollment, Students, Classes

@app.route('/')
def home():
    num_enroll = Enrollment.query.count()
    enrolls = Enrollment.query.all()
    num_studs = Students.query.count()
    studs = Students.query.all()
    num_class = Classes.query.count()
    classes_ = Classes.query.all()
    return render_template('index.html' , num = num_studs, studs = studs, num_class = num_class, classes_ = classes_,  num_enroll = num_enroll, enrolls = enrolls)

@app.route('/search=<keyword>')
def search(keyword):
    data = [str(result) for result in db.session.execute(f"SELECT * FROM todo WHERE desc LIKE '%{keyword}%'")]
    return render_template('searches.html', data = data)

@app.route('/create-student', methods = ['GET', 'POST'])
def create_stud():
    form = AddStud()
    if request.method == 'POST' :
        first_name = form.first_name.data
        surname = form.surname.data
        house_num = form.house_num.data
        postcode = form.postcode.data
        new_stud = Students(first_name = first_name, surname = surname, house_num = house_num, postcode = postcode)
        db.session.add(new_stud)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_stud.html', form = form, ptitle = "Add New Student")

@app.route('/create-class', methods = ['GET', 'POST'])
def create_class():
    form = AddClass()
    if request.method == 'POST' :
        name = form.name.data
        desc = form.desc.data
        new_class = Classes(name = name, desc = desc)
        db.session.add(new_class)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_class.html', form = form, ptitle = "Add New Class")

@app.route('/create-enroll', methods = ['GET', 'POST'])
def create_enroll():
    students = Students.query.all()
    classes_ = Classes.query.all()
    form = AddEnrollment()
    form.fk_student.choices.extend([( student.pk, student.first_name + " " + student.surname) for student in students])
    form.fk_class.choices.extend([( class_.pk, class_.name) for class_ in classes_])
    if request.method == 'POST' :
        fk_student = int(form.fk_student.data)
        fk_class = int(form.fk_class.data)
        new_enroll = Enrollment( fk_student = fk_student, fk_class = fk_class)
        db.session.add(new_enroll)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_enrollment.html', form = form)

@app.route('/update_stud/<int:pk>',methods=['GET', 'POST'])
def update_stud(pk): 
    stud = Students.query.get(pk)
    form = AddStud()
    if request.method == 'POST' :
        stud.first_name = form.first_name.data
        stud.surname = form.surname.data
        stud.house_num = form.house_num.data
        stud.postcode = form.postcode.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_stud.html', form = form, ptitle = "Update Student") 

@app.route('/update_class/<int:pk>',methods=['GET', 'POST'])
def update_class_(pk): 
    class_ = Classes.query.get(pk)
    form = AddClass()
    if request.method == 'POST' :
        class_.name = form.name.data
        class_.desc = form.desc.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_class.html', form = form, ptitle = "Update Class") 

@app.route('/update_enroll/<int:pk>', methods = ['GET', 'POST'])
def update_enroll(pk):
    enroll = Enrollment.query.get(pk)
    students = Students.query.all()
    classes = Classes.query.all()
    form = AddEnrollment()
    form.fk_student.choices.extend([( student.pk, student.first_name + " " + student.surname) for student in students])
    form.fk_class.choices.extend([( class_.pk, class_.name) for class_ in classes])
    if request.method == 'POST' :
        enroll.fk_student = int(form.fk_student.data)
        enroll.fk_class = int(form.fk_class.data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_enrollment.html', form = form, ptitle = "Update Enrollment")


@app.route('/delete_stud/<int:pk>',  methods = ['GET', 'POST'])
def del_stud(pk):
    stud = Students.query.get(pk)
    form = AddStud()
    if request.method == 'POST' :
        db.session.delete(stud)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_stud.html', form = form, stud = stud,  ptitle = "Delete Student")

@app.route('/delete_class/<int:pk>',  methods = ['GET', 'POST'])
def del_class(pk):
    class_ = Classes.query.get(pk)
    form = AddClass()
    if request.method == 'POST' :
        db.session.delete(class_)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_class.html', form = form, class_ = class_,  ptitle = "Delete Class")

@app.route('/delete_enroll/<int:pk>',  methods = ['GET', 'POST'])
def del_enroll(pk):
    enroll = Enrollment.query.get(pk)
    students = Students.query.all()
    classes = Classes.query.all()
    form = AddEnrollment()
    form.fk_student.choices.extend([( student.pk, student.first_name + " " + student.surname) for student in students])
    form.fk_class.choices.extend([( class_.pk, class_.name) for class_ in classes])
    if request.method == 'POST' :
        enroll.fk_student = int(form.fk_student.data)
        enroll.fk_class = int(form.fk_class.data)
        db.session.delete(enroll)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_enrollment.html', form = form, enroll = enroll,  ptitle = "Delete Enrollment")