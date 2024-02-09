from App.database import db

class CoursePlanBridge(db.Model):
    __tablename__="coursePlanBridge"
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    coursePlan = db.Column(db.Integer, db.ForeignKey('course_plans.id'), nullable=False)
    