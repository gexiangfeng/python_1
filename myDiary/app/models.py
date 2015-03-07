from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class Diary(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titlename = db.Column(db.String(128), index = True)
    content = db.Column(db.String(2048), index = True)
    update_time = db.Column(db.DateTime)

    def __repr__(self):
        return '<Diary %r>' % (self.titlename)
