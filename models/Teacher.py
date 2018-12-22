from configs.database import db


class Teacher(db.Model):

    """
    The model of teachers
    """

    __tablename__ = 'teacher'

    id = db.Column(db.Integer, nullable=False, primary_key=True)

    name = db.Column(db.String(20), nullable=False)

    teacher_id = db.Column(db.String(20), nullable=False)

    password = db.Column(db.String(20), nullable=False)

    candidates = db.relationship('Candidate', backref='teacher', lazy=True)

    permission_id = db.Column(db.Integer, db.ForeignKey('permission.id'))
