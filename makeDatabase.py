import hashlib
from models import User, db
db.drop_all()
db.create_all()


# create admin
password = hashlib.md5(str('admin').encode('utf-8')).hexdigest()
admin_user = User('cjkellett@hotmail.co.uk', password)

db.session.add(admin_user)
db.session.commit()
