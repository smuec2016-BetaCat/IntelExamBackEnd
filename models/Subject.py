from configs.database import db


class Subject(db.Model):

    """
    The model of the subject
    """

    __tablename__ = 'subject'

    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)

    subject = db.Column(db.String(50), unique=True)

    vedios = db.relationship('Vedio', backref='subject', lazy=True)
