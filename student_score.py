# Task: A program using a function that takes a list of student scores
# and returns the average, highest and lowest using tuple unpacking. 

def student_scores(scores):
    
    avg = round(sum(scores) / len(scores))
    highest = max(scores)
    lowest = min(scores)
    return avg, highest, lowest
    
    
overall_score  = [10, 30, 20, 50,100, 60, 80, 95, 90, 70, 75, 40]
avg, highest, lowest = student_scores(overall_score)
print(f"{avg} is the average score.")
print(f"{highest} is the highest score.") 
print(f"{lowest} is the lowest score.")
