#grade calculator by Ryan Pham 2024
def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    student_name = input("Enter your name please: ")

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    #prompt user for their math score and changes from string to float.
    math_score = input("Enter your math score please: ")
    math_score = float(math_score)

    #prompt user for their science score and changes from string to float.
    science_score = input("Enter your science score please: ")
    science_score = float(science_score)

    #prompt user for their english score and changes from string to float.
    english_score = input("Enter your english score please: ")
    english_score = float(english_score)

    # Calculate the average grade
    total_grade = english_score + math_score + science_score
    average_grade = total_grade / 3
    # Return the student's name and their average grade
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print (f'{student_name} got an average of: {average_grade}')