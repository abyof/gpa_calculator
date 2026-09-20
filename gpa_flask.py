from flask import Flask, request, render_template
app = Flask(__name__)

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

def calculate_gpa(credits, grade_values):
        total_credits = sum(credits)
        total_sum = sum(c*g for c,g in zip (credits, grade_values))
        final_gpa = total_sum / total_credits
        return total_credits, total_sum, final_gpa

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

@app.route("/")
def home():
    return render_template("gpa_input.html")

@app.route("/info", methods= ['POST'])
def info():
    s_name = request.form.get("s_name", "")

    subjects = request.form.getlist("subject")
    credits = request.form.getlist("credit_hour")
    grades = request.form.getlist("grade")

    try:

        if len(subjects) <=1 or not len(subjects) == len(credits) == len(grades):
            return "Please fill equal subjects, credtis and grades respectively."

        credits = [int(credit) for credit in credits]

        if any(credit <= 0 for credit in credits):
            return "Credit hour must not greater than 0."
        
        grade_values = []

        for grade in grades:
            value = grade_value(grade)
            if value is None:
                return f"Invalid grade: {grade}."
            grade_values.append(value)
        
        total_credits, total_sum, final_gpa = calculate_gpa(credits, grade_values)
        final_gpa = round(final_gpa, 2)
        comment = gpa_comment(final_gpa)
        
    except (ValueError, TypeError, ZeroDivisionError):
        return "Unexpected error occured. please insert only the desired inputs."
    return render_template("gpa_jinja.html", s_name= s_name, subjects= subjects, credits= credits, grades= grades,
        total_credits= total_credits, total_sum= total_sum, final_gpa= final_gpa, comment= comment)

if __name__ == "__main__":
    app.run(debug=True)
    