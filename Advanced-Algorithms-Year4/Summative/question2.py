
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



print(gradingStudents(57))
print(gradingStudents(73))
print(gradingStudents(67))
print(gradingStudents(38))
print(gradingStudents(33))
print(gradingStudents(60))





def gradesystem(grades):
    n = len(grades)
    out = [] # new array of grades 
    for i in range(n):
        grade = grades[i]
        if grade >= 38:
            if grade % 5:# if not multiple of five
                next_grade = ((grade // 5) * 5) + 5 #changed
                if (next_grade - grade) < 3: # simplified 
                    out.append(next_grade)
                    continue # when a grade is changed we go to the next grade and we wont need to go to line 39
        out.append(grade) # append the original grade if the grade did not change or is less than 38
    return out

grades = [50,  57, 73, 67, 38, 33, 60]
print(gradesystem(grades))