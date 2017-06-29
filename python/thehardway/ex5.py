name = "Gabriel V. Evanoff"
age = 35 #not a lie
height = 73 # inches
weight = 175 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'
cm_height = height * 2.54
kg_weight = weight * 0.453592

print "Let's talk about %s." % name
print "He's %d inches tall which is %d cm." % (height, cm_height)
print "He's %d pounds heavy-- or %d kg." % (weight, kg_weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the wine." % teeth

#This line is tricky
print "IF I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
