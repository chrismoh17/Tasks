from App.database import db


class Semester(db.Model):
    __tablename__ = 'semesters'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(2))
    number = db.Column(db.Integer)
    year = db.Column(db.Integer)

    course_plans = db.relationship('CoursePlan', backref='semesters', lazy=True)
    courses = db.relationship('Course', secondary="semester_course", back_populates='semesters', lazy=True)

    def __init__(self, sem_id, sem_title, number, year):
        self.id = sem_id
        self.title = sem_title
        self.number = number
        self.year = year
        

        
        
