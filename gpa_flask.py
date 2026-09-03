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
        grade_values = []

        credit_1 = int(cr_1)
        credit_2 = int(cr_2)
        credit_3 = int(cr_3) 

        if credit_1 <= 0:
            return "credit hour must be positve integer."
        else:
            credits.append(credit_1)
        if credit_2 <= 0:
            return "credit hour must be positive integer."
        else:   
            credits.append(credit_2)
        if credit_3 <= 0:    
            credits.append(credit_3)

        for grade in grades:

            if grade in  ["A+", "A"]:
                grade_values.append(4)
            elif grade == "A-":
                grade_values.append(3.75)
            elif grade == "B+":
                grade_values.append(3.5)
            elif grade == "B":
                grade_values.append(3)
            elif grade == "B-":
                grade_values.append(2.75)
            elif grade == "C+":
                grade_values.append(2.5)
            elif grade == "C-":
                grade_values.append(2)
            elif grade == "D":
                grade_values.append(1)
            elif grade == "F":
                grade_values.append(0)
            else:
                raise ValueError

        total_credits = sum(credits) 
        total_sum = sum(c*g for c,g in zip (credits, grade_values))
        final_gpa = total_sum / total_credits
        gpas = []
        if final_gpa == 4:
            
            gpas.append("🏆MAGNIFICENT")
        elif 3.75 < final_gpa <4:
            gpas.append("⭐EXCELLENT")
        elif 3.5 < final_gpa <= 3.75:
            gpas.append("🟢VERY GOOD")
        elif 3.2 < final_gpa <= 3.5:
            gpas.append("😊GOOD")
        elif 2.75 < final_gpa <= 3.2:
            gpas.append("😐AVERAGE")
        elif 2.5 < final_gpa <= 2.75:
            gpas.append("📉BELOW AVERAGE")
        elif 2 < final_gpa <= 2.5:
            gpas.append("🔴POOR")
        elif 1 < final_gpa <= 2:
            gpas.append("👎VERY POOR")
        else:
            gpas.append("🚫FAIL")

    except (ValueError, TypeError, ZeroDivisionError):
        return "Unexpected error occured. please insert only the desired inputs."
    return render_template("gpa_jinja.html", s_name= s_name, subject_1= subject_1, cr_1= cr_1, grade_1= grade_1,
        subject_2= subject_2, cr_2= cr_2, grade_2= grade_2,subject_3= subject_3, cr_3= cr_3, grade_3= grade_3, total_credits= total_credits, total_sum= total_sum, final_gpa= final_gpa,gpas= gpas)

if __name__ == "__main__":
    app.run(debug=True)
    