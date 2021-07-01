from treasure import db
from treasure.models import Questions


ques4 = Questions(id = 4,quest = 'Swiggy most popular add-on, American staple inspired from Chinese cuisine', answer = 'ketchup')
ques5 = Questions(id = 5,quest = 'A Super acquirement', answer = 'suprdaily')
ques6 = Questions(id = 6,quest = 'The most creative way to stop online abuse', answer = 'whatthefalooda')
ques7 = Questions(id = 7,quest = 'Once a wise person said - One benefit of social distancing is the distance', answer = 'davidzakkam')
ques8 = Questions(id = 8,quest = 'This is still given as an example for - Stand Up, Disagree and Commit', answer = 'thebowlcompany')
ques9 = Questions(id = 9,quest = 'You only connect with IT when something goes wrong', answer = 'zoho')
ques10 = Questions(id = 10,quest = 'Shaadi Teri Bajayenge Hum Band', answer = 'nareshgossain')

db.session.add(ques4)
db.session.add(ques5)
db.session.add(ques6)
db.session.add(ques7)
db.session.add(ques8)
db.session.add(ques9)
db.session.add(ques10)
db.session.commit()