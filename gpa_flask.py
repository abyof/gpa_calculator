from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("gpa_input.html")

@app.route("/info", methods= ['POST'])
def info():
    s_name = request.form.get("s_name", "")

    subject_1 = request.form.get("subject_1", "")
    cr_1 = request.form.get("cr_1", "")
    grade_1 = request.form.get("grade_1", "")

    subject_2 = request.form.get("subject_2", "")
    cr_2 = request.form.get("cr_2", "")
    grade_2 = request.form.get("grade_2", "")

    subject_3 = request.form.get("subject_3", "")
    cr_3 = request.form.get("cr_3", "")
    grade_3 = request.form.get("grade_3", "")

    try:

        credits = []
        grades = [grade_1, grade_2, grade_3]

        credit_1 = int(cr_1)
        credit_2 = int(cr_2)
        credit_3 = int(cr_3) 

        if credit_1 <= 0:
            return "credit hour_1 must be a positive integer."
        
        elif credit_2 <= 0:
            return "credit hour_2 must be a positive integer."
       
        elif credit_3 <= 0:    
            return "credit hour_3 must be a positive integer."
        else:
            credits.append(credit_1)
            credits.append(credit_2)
            credits.append(credit_3)

        def grade_value(grade):
            if grade in ["A+", "A"]:
                return 4
            elif grade == "A-":
                return 3.75
            elif grade == "B+":
                return 3.5
            elif grade == "B":
                return 3
            elif grade == "B-":
                return 2.75
            elif grade == "C+":
                return 2.5
            elif grade == "C":
                return 2
            elif grade == "C-":
                return 1.75
            elif grade == "D":
                return 1 
            elif grade == "F":
                return 0
            else:
                return None
            
        grade_values = []
        for grade in grades:
            value = grade_value(grade)
            grade_values.append(value)

        def calculate_gpa(credits, grade_values):
            total_credits = sum(credits)
            total_sum = sum(c*g for c,g in zip (credits, grade_values))
            final_gpa = total_sum / total_credits
            return total_credits, total_sum, final_gpa 
        total_credits, total_sum, final_gpa = calculate_gpa(credits, grade_values)
        final_gpa = round(final_gpa, 2)
    
        gpas = []
        def gpa_comment(final_gpa):
            if final_gpa == 4:
                return ("🏆MAGNIFICENT")
            elif 3.75 < final_gpa <4:
                return ("⭐EXCELLENT")
            elif 3.5 < final_gpa <= 3.75:
                return ("🟢VERY GOOD")
            elif 3.2 < final_gpa <= 3.5:
                return ("😊GOOD")
            elif 2.75 < final_gpa <= 3.2:
                return ("😐AVERAGE")
            elif 2.5 < final_gpa <= 2.75:
                return ("📉BELOW AVERAGE")
            elif 2 < final_gpa <= 2.5:
                return ("🔴POOR")
            elif 1 < final_gpa <= 2:
                return ("👎VERY POOR")
            else:
                return ("🚫FAIL")
        comment = gpa_comment(final_gpa)
        gpas.append(comment)
        
    except (ValueError, TypeError, ZeroDivisionError):
        return "Unexpected error occured. please insert only the desired inputs."
    return render_template("gpa_jinja.html", s_name= s_name, subject_1= subject_1, cr_1= cr_1, grade_1= grade_1,
        subject_2= subject_2, cr_2= cr_2, grade_2= grade_2,subject_3= subject_3, cr_3= cr_3, grade_3= grade_3, total_credits= total_credits, total_sum= total_sum, final_gpa= final_gpa,gpas= gpas)

if __name__ == "__main__":
    app.run(debug=True)