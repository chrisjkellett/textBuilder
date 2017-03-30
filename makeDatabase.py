import hashlib
from models import User, Savetext, db
db.drop_all()
db.create_all()


# create admin
password = hashlib.md5(str('admin').encode('utf-8')).hexdigest()
username = 'cjkellett'
admin_user = User('cjkellett@hotmail.com', password, username)
admin_user.active = True
db.session.add(admin_user)
db.session.commit()

#create sample text for admin
sText = """India’s foreign affairs minister has condemned “deplorable” race riots targeting African students near Delhi this week that put two men in hospital.

The victims included a Kenyan woman who alleges she was pulled from a rickshaw on Wednesday morning and beaten by a group of men.

Police have arrested at least 600 people they say were involved in the mob violence on Monday in and around Noida, a satellite city to the east of Delhi.

Resentment towards Africans, thousands of whom study in Indian universities, has simmered in India in the past few years, fuelled partly by cultural differences and the involvement of a small proportion of people from the continent in the Delhi drug trade."""

sample_text = Savetext('Indian targets muslims', sText, 1)
db.session.add(sample_text)
db.session.commit()


