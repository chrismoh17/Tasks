from App.database import db

class courseProgram(db.Model):
    __tablename__ = 'course_programs'
    id = db.Column(db.Integer, primary_key=True)
    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    course_type = db.Column(db.String)
    l1Core = db.Column(db.Integer)
    advCore = db.Column(db.Integer)
    l1Elective = db.Column(db.Integer)
    advElective = db.Column(db.Integer)
    found = db.Column(db.Integer)

    def __init__(self, program_id, course_id):
        self.program_id = program_id
        self.course_id = course_id
