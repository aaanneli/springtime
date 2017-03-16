import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 		 			      'springtimeproject.settings')

import django
django.setup()

from springtime.models import UserProfile, Review, Trampoline, Booking

def populate():

#Trampoline categories, ID, broken or not
    Tramp_cat = [
        {"trampolineID": "per12345", 
	 "broken": False, 
	 "category" : "Performance"}, 
	{"trampolineID": "cir02468", 
	 "broken": False, 
	 "category" : "Cirular"},
	{"trampolineID": "rec13579", 
	 "broken": True, 
	 "category" : "Rectangular"},
	{"trampolineID": "per54321", 
	 "broken": True, 
	 "category" : "Performance"},
	{"trampolineID": "cir01468", 
	 "broken": False, 
	 "category" : "Cirular"},
	{"trampolineID": "rec12579", 
	 "broken": False, 
	 "category" : "Rectangular"}]

    for cat in Tramp_cat:
        c = add_tramp(cat["trampolineID"], cat["broken"], cat["category"])
        
#Reviews, not including username or rating 
    Reviews = [
	{"content": "Easy booking, lots of fun!"}, 
	{"content": "Best day of my life!"},
	{"content": "Will come back!"}, 
	{"content": "I broke my face, but the proffesional team 	at Soring Time took good care of me. My face is recovering."},
	{"content": "Worst experience of my life"}, 
	{"content": "I didn't want my kids back, could you keep 	them please?"}]

def add_review(revNumber, time, userID, content, rating):
    print "adding review"
    r = Review.objects.get_or_create(review=revNumber, content=content)[0]
    r.content=content
    r.rating=rating
    r.save()
    return r

def add_tramp(trampolineID, broken, category):
    print "adding tramp"
    t = Trampoline.objects.get_or_create(trampolineID=trampolineID)[0]
    t.broken = broken
    t.category=category
    t.save()
    return t

#Start execution here!
if __name__ == '__main__':
    print ("Starting Spring Time population script...")
    populate()
