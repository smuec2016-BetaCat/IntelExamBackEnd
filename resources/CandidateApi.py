from models.permission import Permission
from models.Teacher import Teacher
from models.Candidate import Candidate
from flask_restful import Resource
from configs.database import to_dict
from flask import request
from configs.database import db

class CandidateApi(Resource):
    """
    :return the information of candidates
    """
    @staticmethod
    def get():
        """
        Get the information of users
        :return: user information
        """
        try:
            first_candidate = Candidate.query.filter(Candidate.examination_status == 0)\
                .filter(Candidate.teacher_id == 1).first()
            print(first_candidate)
            first_candidate = to_dict(first_candidate)
        except KeyError:
            return {"error": "error"}, 500
        except AttributeError:
            return {"information": "null"}, 200
        return {"information": first_candidate}, 200

    @staticmethod
    def post():
        """
        add grade and change status of candidates
        :return: succeed or failed
        """
        try:
            response = request.get_json()
            candidate_id = response["id"]
            result = Candidate.query.filter(Candidate.id == candidate_id).first()
            result.grades = response["grade"]
            result.examination_status = response["status"]
            db.session.commit()
        except KeyError:
            return {"error": "failed"}, 500
        return {"information": "succeed"}, 200

