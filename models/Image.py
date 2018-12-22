from configs.database import db


class Image(db.Model):

    """
    The model of the image
    """

    __tablename__ = 'image'

    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)

    url = db.Column(db.String(255), unique=True)
