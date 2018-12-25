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
            id = 310102199807223300
            ticket = 6551310015040400
            first_name = ["张", "杨", "李", "丁", "王", "蒋", "吕", "赵", "奚", "陆"]
            sex = ["男", "女"]
            school = ["上海海事大学", "上海大学", "上海海洋大学", "上海交通大学",
                      "上海复旦大学", "上海纽约大学", "上海同济大学",
                      "上海华东师范大学", "上海华东政法大学", "上海华东理工大学"]
            for i in range(20):
                a = int(random.random() * 10)
                b = int(random.random() * 10)
                c = round(random.random())
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
                               name=first_name[a] + str1 + str2,
                               sex=sex[c],
                               email='admin@example.com',
                               phone="18717744742",
                               address=school[b],
                               examination_time="2018-12-21 21:30:00",
                               examination_status=0,
                               teacher_id=1,
                               vedio_id=1,
                               photo_id=1
                               )
                db.session.add(me)
                db.session.commit()
        except KeyError:
            return {"error": "error"}, 500
        except AttributeError:
            return {"information": "null"}, 200
        return {"information": "succeed"}, 200




