from App.database import db
from App.models import courseProgram

class CourseProgramController:
    def create_course_program(self, program_id, course_id, course_type):
        program = courseProgram(program_id=program_id, course_id=course_id, course_type=course_type)
        db.session.add(program)
        db.session.commit()
        return program

    def get_course_program_by_id(self, program_id):
        return courseProgram.query.get(program_id)

    def get_course_programs_by_course_id(self, course_id):
        return courseProgram.query.filter_by(course_id=course_id).all()

    def get_course_programs_by_program_id(self, program_id):
        return courseProgram.query.filter_by(program_id=program_id).all()

    def delete_course_program(self, program_id):
        program = courseProgram.query.get(program_id)
        if program:
            db.session.delete(program)
            db.session.commit()
            return True
        return False
