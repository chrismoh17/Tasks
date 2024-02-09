from App.database import db

class studentCourse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    grade = db.Column(db.Integer)
    year = db.Column(db.Integer)
    complete = db.Column(db.String(3))
