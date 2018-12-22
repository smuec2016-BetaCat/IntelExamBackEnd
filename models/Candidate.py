from configs.database import db


class Candidate(db.Model):

    """
    The model of the candidates
    """

    __tablename__ = 'candidate'  # name the candidate

    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)

    identity_number = db.Column(db.String(20), nullable=False, unique=True)

    ticket_number = db.Column(db.String(20), nullable=False, unique=True)

    name = db.Column(db.String(64), unique=True, nullable=False)

    sex = db.Column(db.String(10), nullable=False)

    age = db.Column(db.Integer)

    phone = db.Column(db.String(20), nullable=False)

    address = db.Column(db.String(50), nullable=False)

    email = db.Column(db.String(64), nullable=False)

    examination_time = db.Column(db.DateTime, nullable=False)

    grades = db.Column(db.Integer)

    vedio_id = db.Column(db.Integer, db.ForeignKey('vedio.id'), nullable=False)

    examination_status = db.Column(db.Integer, nullable=False, default=0)

    photo_id = db.Column(db.ForeignKey('image.id'), nullable=False)

    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
