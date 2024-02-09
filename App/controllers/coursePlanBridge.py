from App.database import db
from App.models import CoursePlanBridge

class CoursePlanBridgeController:
    def create_course_plan_bridge(self, course_id, course_plan_id):
        bridge = CoursePlanBridge(course=course_id, coursePlan=course_plan_id)
        db.session.add(bridge)
        db.session.commit()
        return bridge

    def get_course_plan_bridge_by_id(self, bridge_id):
        return CoursePlanBridge.query.get(bridge_id)

    def get_course_plan_bridges_by_course_id(self, course_id):
        return CoursePlanBridge.query.filter_by(course=course_id).all()

    def get_course_plan_bridges_by_course_plan_id(self, course_plan_id):
        return CoursePlanBridge.query.filter_by(coursePlan=course_plan_id).all()

    def delete_course_plan_bridge(self, bridge_id):
        bridge = CoursePlanBridge.query.get(bridge_id)
        if bridge:
            db.session.delete(bridge)
            db.session.commit()
            return True
        return False
