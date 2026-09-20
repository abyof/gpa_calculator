console.log("Javascript is working!")
const button = document.getElementById("add");
const table = document.getElementById("table-body");

button.addEventListener("click", function(){
    console.log("Add_row button is clicked!")
    const row = document.createElement("tr");

    const cell_1 = document.createElement("td");
    const cell_2 = document.createElement("td");
    const cell_3 = document.createElement("td");
    const removeCell = document.createElement("td");
    const removeButton = document.createElement("button");
    
    const input_1 = document.createElement("input");
    const input_2 = document.createElement("input");
    const input_3 = document.createElement("select");

    input_1.type= "text";
    input_1.name= "subject";

    input_2.type= "number";
    input_2.name= "credit_hour";
    input_2.classList.add("cr-input");

    input_3.name = "grade";
    input_3.classList.add("grd-input")
    
    const grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]
    grades.forEach(function(gradevalue){
        const option = document.createElement("option");
        option.type = gradevalue;
        option.textContent = gradevalue;
        input_3.appendChild(option);
    })

    row.appendChild(cell_1);
    row.appendChild(cell_2);
    row.appendChild(cell_3);
    table.appendChild(row);

    cell_1.appendChild(input_1);
    cell_2.appendChild(input_2);
    cell_3.appendChild(input_3);

    removeButton.type= "button";
    removeButton.textContent= "Remove_row";

    row.appendChild(removeCell);
    removeCell.appendChild(removeButton);

    removeButton.addEventListener("click", function(){
        console.log("Remove button is clicked!")
        removeButton.parentElement.parentElement.remove("td");
    });

});