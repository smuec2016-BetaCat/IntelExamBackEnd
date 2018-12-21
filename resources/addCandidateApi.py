from configs.database import db
from models.Candidate import Candidate
from flask_restful import Resource
import random


class addCandidateApi(Resource):
    """
    :return the information of candidates
    """
    @staticmethod
    def get():
        """
        add infromation of Candidates
        """
        try:
            id = 310102199807223109
            ticket = 6551310015040270
            for i in range(10):
                id = id+2
                ticket= ticket+2
                head1 = random.randint(0xb0, 0xf7)
                body1 = random.randint(0xa1, 0xfe)
                val1 = f'{head1:x}{body1:x}'
                str1 = bytes.fromhex(val1).decode('gb2312')
                head2 = random.randint(0xb0, 0xf7)
                body2 = random.randint(0xa1, 0xfe)
                val2 = f'{head2:x}{body2:x}'
                str2 = bytes.fromhex(val2).decode('gb2312')
                me = Candidate(identity_number=id,
                               ticket_number=ticket,
                               name="杨" + str1 + str2,
                               sex='男',
                               email='admin@example.com',
                               phone="18717744742",
                               address=str1 + str2 +"大学",
                               examination_time="2018-12-21 21:30:00",
                               examination_status=0,
                               teacher_id=1
                               )
                db.session.add(me)
                db.session.commit()
        except KeyError:
            return {"error": "error"}, 500
        except AttributeError:
            return {"information": "null"}, 200
        return {"information": "succeed"}, 200




