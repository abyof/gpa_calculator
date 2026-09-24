# GPA Calculator 🎓

A simple GPA Calculator built with **Python (Flask), HTML, CSS, and JavaScript**.

## Features

* Add and remove course rows
* Enter subjects, credit hours, and grades
* Automatically calculate GPA
* Display total credits and grade points
* Show a GPA-based performance comment
* Input validation and error handling

## Programming languages/technologies used

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)

![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)

![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)

## Project Structure

```text
GPA-Calculator/
├── gpa_flask.py
├── templates/
│   ├── gpa_input.html
│   └── gpa_jinja.html
├── static/
    ├── css/                
       └── gpa.css
       └── gpa_view.css
    ├── script/
       └── gpa_script.js
└── README.md
└── requirements.txt
```

## How It Works

The user enters their subjects, credit hours, and grades through the HTML interface. **Flask/Python** processes the submitted data, calculates the GPA, and sends the result to a Jinja template. **JavaScript** is used for adding and removing course rows, while **CSS** handles the design.

## Project Status

Learning project — continuously improving as I learn more about Python, Flask, and web development.