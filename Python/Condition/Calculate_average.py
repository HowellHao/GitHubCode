def Calculate_average(score):
    return sum(score) / len(score)
def classify_students(grades):
    if grades >= 9.7:
        return "A+"
    elif 9.3 <= grades < 9.7:
        return "A"
    elif 9 <= grades < 9.3:
        return "A-"
    elif 8.7<= grades < 8.9:
        return "B+"
    elif 8.3 <= grades < 8.7:
        return "B"
    elif 8 <= grades < 8.3:
        return "B-"
    elif 7.7<= grades < 7.9:
        return "C+"
    elif 7.3 <= grades < 7.7:
        return "C"
    elif 7 <= grades < 7.3:
        return "C-"
    else:
        return "Fail"
try:
    scores=[]
    number_subjects = int (input("Insert Subject Numbers: "))
    if 0 > number_subjects:
        print("Invalid number of subjects")
    else:
        for i in range (number_subjects):
            score = float(input(f"Insert score for subject {i+1}: "))
            if 10 < score or score < 0:
                print("Invalid score")
                break
            scores.append(score)
            print(scores)
        if len(scores) == number_subjects:
            average_score = Calculate_average(scores)
            classification = classify_students(average_score)
            print(f"Average score: {average_score: .2f}")
            print("Classification :", classification)
except ValueError:
    print("Invalid input")