
from datetime import datetime
now = datetime.now()
print now

print now.year
print now.month
print now.day
print '%s/%s/%s' % (now.year, now.month, now.day)
print '%s:%s:%s' % (now.hour, now.minute, now.second)
print '%s/%s/%s %s:%s:%s' % (now.year, now.month, now.day, now.hour, now.minute, now.second)

my_string = "new string"
print len(my_string)
print my_string.upper()
print my_string.lower()


name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." %(name, quest, color)

