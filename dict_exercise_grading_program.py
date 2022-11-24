scores = {
	"aditya" : 71,
	"sanya" : 88,
	"ayush" : 98,
	"priyanshi" : 50,
	"kartik" : 33,
	"rahul" : 94,
	"yash" : 20
}
print(scores)

student_grades = {}

for score in scores :
	marks = scores[score]
	print(marks)

	if marks < 30 :
		scores[score] = "poor"
	elif marks >30 and marks<70 :
		scores[score] = "okay"
	elif marks >70 :
		scores[score] = "good"

print(scores)

