import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 		 			      'springtimeproject.settings')

import django
django.setup()

from datetime import datetime
from django.contrib.auth.models import User
from springtime.models import UserProfile, Review, Trampoline, Booking, Category

def populate():

#Trampoline categories, ID, broken or not
    Performance_Tramp = [
    {"trampolineID": "per12345",
	 "broken": False},
    {"trampolineID": "per54321",
	 "broken": True}]

    Rectangular_Tramp = [
	{"trampolineID": "rec13579",
	 "broken": True},
	{"trampolineID": "rec12579",
	 "broken": False}]

    Circular_Tramp = [
    {"trampolineID": "cir02468",
	 "broken": False},
    {"trampolineID": "cir01468",
	 "broken": False}]

    theresa = add_user("TheresaMay", "123456", True, False)
    nicola = add_user("NicolaSturgeon", "123456", False, False)
    david = add_user("DavidCameron", "123456", False, False)
    donald = add_user("DonaldTrump", "123456", False, False)
    vladimir = add_user("VladimirPutin", "123456", True, True)
    barack = add_user("BarackObama", "123456", False, False)
    hilary = add_user("HilaryClinton","123456", False, False)

#Creating main tramppoline categories
    Category = [
    {"name": "Performance","trampoline":Performance_Tramp},
    {"name": "Rectangular", "trampoline": Rectangular_Tramp},
    {"name": "Circular", "trampoline":Circular_Tramp}]


#Reviews, not including username
    Reviews = [
    {"userID": theresa, "content": "Easy booking, lots of fun!", "rating": 5},
    {"userID": nicola, "content": "Will come back!", "rating": 5},
    {"userID": david,
     "content": "I broke my face, but the professional team at Spring Time took good care of me. My face is recovering.", "rating": 5},
    {"userID": barack, "content": "Worst experience of my life", "rating": 1},
    {"userID": hilary, "content": "I didn't want my kids back, could you keep them please?", "rating": 3}]

    tramp_list = []
    for cat in Category:
        c=add_cat(cat["name"])
        for tramp in cat["trampoline"]:
            tramp_list.append(add_tramp(tramp["trampolineID"],tramp["broken"], c))

    for review in Reviews:
        r = add_review(review["userID"] , review["content"], review["rating"])

    add_booking(hilary, tramp_list[0], datetime.now())
    add_booking(donald, tramp_list[3], datetime.now())
    add_booking(barack, tramp_list[4], datetime.now())
    add_booking(vladimir, tramp_list[5], datetime.now())

# Print out the categories we have added
for c in Category.objects.all():
    for p in Trampoline.objects.filter(category=c):
        print ("- {0} - {1}".format(str(c), str(p)))

def add_review(userID, content, rating):
    print "adding review"
    r = Review.objects.get_or_create(userID=userID, content=content, rating=rating)[0]
    r.content=content
    r.rating=rating
    r.userID=userID
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

def add_user(username, password, is_staff, is_admin):
    print "\tadding user"
    u=User.objects.get_or_create(username=username)[0]
    u.set_password(password)
    u.save()
    up= UserProfile.objects.get_or_create(user=u)[0]
    up.is_staff=is_staff
    up.is_admin=is_admin
    up.save()
    return u

def add_booking(userID, trampolineID, startTime):
    print "adding bookings"
    b=Booking.objects.get_or_create(trampolineID=trampolineID)[0]
    b.userID.add(userID)
    #b.trampolineID.add(trampolineID)
    b.startTime=startTime
    b.save()
    return b


#Start execution here!
if __name__ == '__main__':
    print ("Starting Spring Time population script...")
    populate()