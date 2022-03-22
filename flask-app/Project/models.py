from Project import db

class Students(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    house_num= db.Column(db.Integer)
    postcode = db.Column(db.String(8)) 
    stu_enroll = db.relationship('Enrollment', backref = 'students')
    def __str__(self):
        return f"{self.first_name} {self.surname} lives at {self.house_num} {self.postcode}"

class Enrollment(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    fk_student = db.Column(db.Integer, db.ForeignKey("students.pk"))
    fk_class = db.Column(db.Integer, db.ForeignKey("classes.pk"))
    def __str__(self):
        return f"{self.fk_student}, is enrolled in {self.fk_class}"

class Classes(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    c_name = db.Column(db.String(255))
    c_desc = db.Column(db.String(255))
    class_enroll = db.relationship('Enrollment', backref = 'classes')
    def __str__(self):
        return f"{self.c_name}:\n{self.c_desc}"