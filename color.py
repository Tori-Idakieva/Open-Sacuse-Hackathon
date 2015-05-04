#!/usr/bin/python
import random
import cgi, cgitb
cgitb.enable()
form=cgi.FieldStorage()
ans= form.getvalue("emotion")
#ans2= form.getvalue("continue")
	
a = ["happy","funny", "great", "good", "cheerful", "nice", "pure", "excited", "dreamy", "creative", "inspired", "romantic", "fantastic", "amused", "wonderful", "blessed","sexy"]
b = ["sad", "blue","dark","disappointed", "mysterious", "bad", "tired", "depressed", "down", "bored", "devious", "desperate","dependable", "dull", "smart", "sick", "awful", "nostalgic"]
c = ["angry", "passionate", "important", "positive", "powerful", "determined", "furious", "crazy", "cautious", "in harmony", "loved", "in love", "hopeful", "motivated", "warm and fuzzy", "energetic", "energised", "festive"]
d = ["relaxed", "calm", "stable", "tranquil", "free", "thoughful", "peaceful", "responsible", "motivated", "sleepy", "strong", "emotional"]

	# a - pink and purple b - grey, dark c - yellow and red d - blue and green
	# examples of not included emotions - simple, plain, elegant, warm, cold, wholesome
wear1 = ["Pink", "Beige", "Bisque", "Light blue", "Light pink", "Purple", "Light purple", "White", "Violet"]
wear2 = ["Grey", "Brown", "Sienna", "Maroon", "Dark blue", "Silver", "Denim", "Dark purple", "Dark green"]
wear3 = ["Yellow", "Red", "Golden", "Ochre", "Lemon", "Coral", "Orange", "Magenta", "Lemon yellow", "Wine red", "Amber"]
wear4 = ["Blue", "Azure", "Lime", "Baby blue", "Sky blue", "Sea green", "Green", "Light green"]

def linearSeach(myItem, myList): 
	found = False
	position = 0
	while position < len(myList) and not found:
		if myList[position] == myItem:
			found = True
		position = position + 1
	return found

answer = (ans.lower()).strip()
isitInA = linearSeach(answer, a)
isitInB = linearSeach(answer, b)
isitInC = linearSeach(answer, c)
isitInD = linearSeach(answer, d)

print "Content-Type:text/html;charset=utf-8"
print ""
print "<html>"
print "<head>"
print"<link rel='stylesheet' type='text/css' href='https://project.cs.cf.ac.uk/IdakievaVD/color.css'/>"
print"<title>Emotion colors</title>"
print"</head>"
print "<body>"
print "<p>"
if isitInA == True or isitInB == True or isitInC == True or isitInD == True:	
	if isitInA: 
		feel = random.choice(wear1)
		print("<h1>Your clothes should be in this color:</h1>")
		print("<p>" + feel + "</p>")
	if isitInB:
		feel = random.choice(wear2)
		print("<h1>Your clothes should be in this color:</h1>")
		print("<p>" + feel + "</p>")
	if isitInC:
		feel = random.choice(wear3)
		print("<h1>Your clothes should be in this color:</h1>")
		print("<p>" + feel + "</p>")
	if isitInD:
		feel = random.choice(wear4)
		print("<h1>Your clothes should be in this color:</h1>")
		print("<p>" + feel + "</p>")
else:
		print("<h1>I am not familiar with what you are feeling! Sorry.. Try again later!</h1>")
print "<br></br><br>"
print("<p>Click on the picture to play again!</p><br>")
print "<a href = 'https://project.cs.cf.ac.uk/IdakievaVD/colors.html'>"
print "<img id='colors'src='https://project.cs.cf.ac.uk/IdakievaVD/colors.jpg' alt='colors'>"
print "</a>" 
print "</p>"
print "</body>"
print "</html>"
