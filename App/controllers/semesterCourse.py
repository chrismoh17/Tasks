from App.database import db
from App.models import semesterCourse

class SemesterCourseController:
    def create_semester_course(self, course_id, semester_id):
        semester_course = semesterCourse(course_id=course_id, semester_id=semester_id)
        db.session.add(semester_course)
        db.session.commit()
        return semester_course

    def get_semester_course_by_id(self, semester_course_id):
        return semesterCourse.query.get(semester_course_id)

    def get_semester_courses_by_course_id(self, course_id):
        return semesterCourse.query.filter_by(course_id=course_id).all()

    def get_semester_courses_by_semester_id(self, semester_id):
        return semesterCourse.query.filter_by(semester_id=semester_id).all()

    def delete_semester_course(self, semester_course_id):
        semester_course = semesterCourse.query.get(semester_course_id)
        if semester_course:
            db.session.delete(semester_course)
            db.session.commit()
            return True
        return False
