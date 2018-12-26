from models.Teacher import Teacher
from flask_restful import Resource
from configs.database import to_dict
from flask import request
from configs.database import db


class LoginApi(Resource):
    """
    :return the status of Login
    """
    @staticmethod
    def post():
        """
        Login in
        :return: success or error message
        """
        response = request.get_json()
        teacher_id = response["teacher_id"]
        password = response["password"]
        teacher = Teacher.query.filter_by(teacher_id=teacher_id).first()

        if teacher is None:
            return {"error": "teacher doesn't exit!"}, 404
        if teacher.password != password:
            return {"error": "Wrong password"}, 403

        teacher = to_dict(teacher)
        return {"teacher": teacher}, 200




