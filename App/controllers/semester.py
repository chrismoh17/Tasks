from flask import Blueprint, request, jsonify
from App.database import db
from App.models import Semester


def get_semesters():
    semesters = Semester.query.all()
    semesters_list = [
        {'id': semester.id, 'title': semester.title}
        for semester in semesters
    ]
    return jsonify({'semesters': semesters_list})


def get_semester(semester_id):
    semester = Semester.query.get(semester_id)
    if semester:
        return jsonify({'id': semester.id, 'title': semester.title})
    else:
        return jsonify({'error': 'Semester not found'}), 404
    
def get_title (semester_id):
    semester = Semester.query.get(semester_id)
    if semester:
        return semester.title



def create_semester():
    data = request.get_json()
    title = data.get('title')
    semester_id = data.get('semester_id')

    new_semester = Semester(semester_id=semester_id, title=title)

    db.session.add(new_semester)
    db.session.commit()

    return jsonify({'message': 'Semester created successfully'}), 201

def create_semester_new(id, title, number, year):
    course = Semester.query.get(id)
    if course:
        return None
    new_course = Semester(id, title, number, year)
    db.session.add(new_course)
    db.session.commit()
    return new_course

def update_semester(semester_id):
    semester = Semester.query.get(semester_id)
    if not semester:
        return jsonify({'error': 'Semester not found'}), 404

    data = request.get_json()
    semester.title = data.get('title', semester.title)

    db.session.commit()

    return jsonify({'message': 'Semester updated successfully'})


def delete_semester(semester_id):
    semester = Semester.query.get(semester_id)
    if not semester:
        return jsonify({'error': 'Semester not found'}), 404

    db.session.delete(semester)
    db.session.commit()

    return jsonify({'message': 'Semester deleted successfully'})

