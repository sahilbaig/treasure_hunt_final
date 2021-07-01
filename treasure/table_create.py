from treasure import db
from treasure.models import Questions


ques = Questions(id = 3,quest = 'If Gods could cook, this is probably where they will be cooking', answer = 'cloudkitchen')
db.session.add(ques)
db.session.commit()