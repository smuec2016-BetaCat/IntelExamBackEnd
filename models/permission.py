from configs.database import db


class Permission(db.Model):

    """
    The model of permission for permission
    """

    __tablename__ = 'permission'

    id = db.Column(db.Integer, nullable=False, primary_key=True)

    permission = db.Column(db.Integer, nullable=False, default=0)
