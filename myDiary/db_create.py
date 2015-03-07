#!/usr/bin/env python
#from migrate.versioning import api
from app import db,models
import os.path
from datetime import datetime
db.create_all()
di = models.Diary(titlename='first diary',content = 'This is my first diary',update_time=datetime.utcnow())
db.session.add(di)
db.session.commit()
