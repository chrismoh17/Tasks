from App.database import db
from App.models import prerequisites, courseHistory
import json

class Course(db.Model):
    __tablename__='courses'
    id = db.Column(db.String(8), primary_key=True)
    courseTitle = db.Column(db.String(50))
    credits = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    type = db.Column(db.String(5))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    
    course_plans = db.relationship('CoursePlan', secondary="coursePlanBridge",back_populates='courses', lazy=True)
    prereqq = db.relationship('Prerequisites', backref='courses', lazy=True)
    semesters = db.relationship('Semester', secondary="semester_course",back_populates='courses', lazy=True)

    def __init__(self, code, title, credits, ratings, type, department_id):
        self.id = code
        self.courseTitle = title
        self.credits = credits
        self.type = type
        self.rating = ratings
        self.department_id = department_id
        # self.semester_id = semester_id
    
    def get_json(self):
        return{
            'Course Code:': self.id,
            'Course Name: ': self.courseTitle,
            'Course Grade: ': self.grade,
            'No. of Credits: ': self.credits,
            'Course Type: ': self.type,
            'Course rating': self.rating,
            'Semester: ': self.semester,
            'Year: ': self.year,
            'Completed?': self.complete,
            'Prerequisites: ': self.prereq,
            'Course_plan_id':self.course_plan_id
        }
