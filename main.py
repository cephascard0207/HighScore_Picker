#HighScore_Picker
#Created by Cephas Cardozo
#Developed using Python

#welcome_print_statement
print("HighScore_Picker")
print("Created by Cephas Cardozo")
print("Developed using Python\n")

#variable
student_scores = input("Input a list of student scores\nType here: ").split()

#for_loop
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

#print_statement
print(student_scores)

#variable
highest_score = 0

#for_loop & indented_conditional
for score in student_scores:
  if score > highest_score:
    highest_score = score


#print_statement
print(f"The highest score from the list is {highest_score}")