from models.Veido import Vedio
from models.Image import Image
from models.Subject import Subject
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
            # search the first_candidate
            first_candidate = Candidate.query.filter(Candidate.examination_status == 0)\
                .filter(Candidate.teacher_id == 1).first()
            # search the first_candidate_photo
            first_candidate_photo = Image.query\
                .filter(Image.id == first_candidate.photo_id).first()
            # search the first_candidate_vedio
            first_candidate_vedio = Vedio.query\
                .filter(Vedio.id == first_candidate.vedio_id).first()
            # search the first_candidate_subject
            first_candidate_subject = Subject.query\
                .filter(Subject.id == first_candidate_vedio.subject_id).first()
            # turn row into dict
            first_candidate = to_dict(first_candidate)
            first_candidate_photo = to_dict(first_candidate_photo)
            first_candidate_vedio = to_dict(first_candidate_vedio)
            first_candidate_subject = to_dict(first_candidate_subject)
            first_candidate["photo"] = first_candidate_photo
            first_candidate["vedio"] = first_candidate_vedio
            first_candidate["subject"] = first_candidate_subject
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
            return {"error": "failed"}, 406
        return {"information": "succeed"}, 200

