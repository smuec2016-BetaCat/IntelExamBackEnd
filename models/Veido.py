from configs.database import db


class Vedio(db.Model):

    """
    The model of the vedio
    """

    __tablename__ = 'vedio'

    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)

    name = db.Column(db.String(255), nullable=False)

    url = db.Column(db.String(255), unique=True)

    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
