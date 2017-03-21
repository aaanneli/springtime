import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 		 			      'springtimeproject.settings')

import django
django.setup()

from springtime.models import UserProfile, Review, Trampoline, Booking, Category

def populate():

#Trampoline categories, ID, broken or not
    Performance_Tramp = [
    {"trampolineID": "per12345",
	 "broken": False},
    {"trampolineID": "per54321",
	 "broken": True}]

    Circular_Tramp = [
    {"trampolineID": "cir02468",
	 "broken": False},
    {"trampolineID": "cir01468",
	 "broken": False}]

    Rectangular_Tramp = [
	{"trampolineID": "rec13579",
	 "broken": True},
	{"trampolineID": "rec12579",
	 "broken": False}]

#Creating main tramppoline categories
    Category = [
    {"name": "Performance","trampoline":Performance_Tramp},
    {"name": "Rectangular", "trampoline":Rectangular_Tramp},
    {"name": "Circular", "trampoline": Circular_Tramp}]


#Reviews, not including username or rating
    Reviews = [
	{"content": "Easy booking, lots of fun!"},
	{"content": "Best day of my life!"},
	{"content": "Will come back!"},
	{"content": "I broke my face, but the proffesional team at Soring Time took good care of me. My face is recovering."},
	{"content": "Worst experience of my life"},
	{"content": "I didn't want my kids back, could you keep them please?"}]

    for cat in Category:
        c=add_cat(cat["name"])
        for tramp in cat["trampoline"]:
            add_tramp(tramp["trampolineID"],tramp["broken"], c)


# Print out the categories we have added
for c in Category.objects.all():
    for p in Trampoline.objects.filter(category=c):
        print ("- {0} - {1}".format(str(c), str(p)))

def add_review(revNumber, time, userID, content, rating):
    print "adding review"
    r = Review.objects.get_or_create(review=revNumber, content=content)[0]
    r.content=content
    r.rating=rating
    r.save()
    return r

def add_tramp(trampolineID, broken, category):
    print "\tadding tramp"
    t = Trampoline.objects.get_or_create(trampolineID=trampolineID, category=category)[0]
    t.broken = broken
    t.category=category
    t.save()
    return t

def add_cat(name):
    print "adding cat"
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

#Start execution here!
if __name__ == '__main__':
    print ("Starting Spring Time population script...")
    populate()