import pandas as pd
import time 
print("..........SIMPLE GPA CALCULATOR.........")
for  x in range (5,-1,-1):
    second = x%60
    minute = x//60 
    time.sleep(1)
    print(f"\r{minute:02d}:{second:02d}", end= "", flush= True)
print("\r .....Let's go!......")

running = True

while running:

    try:

            n = int(input("how many subjects you want to calculate:"))
        
            courses = []
            credits = []
            grades = []
            grade_values = []

            for x in range(n):
            
                subjects = input(f"subject_{x+1}:")
                k = subjects.strip()
                if not k:
                    raise ValueError("Subject name can't be empty")
                cr_hr = int(input(f"credit_hour_{x+1}:"))
                grade = input(f"grade_{x+1}:").upper()
                    
                courses.append(subjects)
                credits.append(cr_hr)
                grades.append(grade)    

                if grade.upper() in ["A+", "A"]:
                    grade_value = 4 
                elif grade.upper() == "A-":
                    grade_value = 3.75
                elif grade.upper() == "B+":
                    grade_value = 3.5
                elif grade.upper() == "B":
                    grade_value = 3
                elif grade.upper() == "B-":
                    grade_value = 2.75
                elif grade.upper() == "C+":
                    grade_value = 2.5
                elif grade.upper() == "C":
                    grade_value = 2
                elif grade.upper() == "C-":
                    grade_value = 1.75
                elif grade.upper() == "D":
                    grade_value = 1
                elif grade.upper() == "F":
                    grade_value = 0
                else:
                    raise ValueError
                grade_values.append(grade_value)

                data = {
            "|Courses|": courses,
            "|Credit_hours|": credits,
            "|Grades|": grades,
            "|Grade_values|": grade_values
            }
        
            df = pd.DataFrame(data)
            print(df)

            total_credits = sum(credits)

            print(f"total credit_hours = {(total_credits)}")

            total_gpa = sum(c*g for c,g in zip(credits, grade_values))

            grand = total_gpa/total_credits

            print(f".........FINAL_GPA = {grand}........")

            if grand == 4:
                print("🏆Marvellous")
            elif 3.8<=grand<4:
                print("🥇Excellent")
            elif 3.6<=grand<3.8:
                print("🥈Verygood")
            elif 3.5<=grand<3.6:
                print("🥉Good")
            elif 3<=grand<3.5:
                print("🤏🏼not bad")
            else:
                print("🆖Not_enough")
            
    except Exception as e:

        print(f"Error occurred. {e} Try again.")

    if not input("Do you want to try again: (choose yes ✔️ or no ❌ : )").lower() == "yes":
        print("𝓖𝓸𝓸𝓭𝓫𝔂𝓮👋!")
        break
    else:
         continue