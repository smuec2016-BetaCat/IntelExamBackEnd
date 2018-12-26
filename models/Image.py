from configs.database import db


class Image(db.Model):

    """
    The model of the image
    """

    __tablename__ = 'image'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    url = db.Column(db.String(200))
