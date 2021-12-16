import sys
# function takes in a grade and return the 
# appropriate score acording to the defined grading system in the prompt
def gradingStudents(grade):
    if grade < 38:  # check if a grade is less than 38 where we do not need to change anything
        return grade
    if grade % 5: # check if a grade is already a multiple of five which if its the case we do not need to change anything 
        upperbound = ((grade // 5) * 5) + 5 # calculate upper bound which is a multple of 5 
        if upperbound - grade < 3:  # check if the grade deifference is is less than 3, 
            return upperbound  # round grade up to the next multiple of 5.
        else: 
            return grade # rturn grde if the difference if not less than 3 
    return grade  # return grade if the grade is a multiple of five.



def main(grades):
    print("Original grade |  Rounded grades")
    for grade in grades:
        print(grade, "            |     ", gradingStudents(grade))


inpt = open(sys.argv[1]) 
for line in inpt:
    line = line.split()
    grades = [int(i) for i in line]
    print("Running test case where grades are {}".format(line), end="\n\n")
    main(grades)
    print("***********************")