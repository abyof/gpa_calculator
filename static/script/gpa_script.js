const button = document.getElementById("add");
const table = document.getElementById("table-body");

button.addEventListener("click", function(){
    const row = document.createElement("tr");

    const cell_1 = document.createElement("td");
    const cell_2 = document.createElement("td");
    const cell_3 = document.createElement("td");
    const removeCell = document.createElement("td");
    const removeButton = document.createElement("button");
    
    const input_1 = document.createElement("input");
    const input_2 = document.createElement("input");
    const input_3 = document.createElement("input");

    input_1.type= "text";
    input_2.type= "number";
    input_3.type= "text";

    input_1.name = "subject";
    input_2.name = "credit_hour";
    input_3.name = "grade";

    row.appendChild(cell_1);
    row.appendChild(cell_2);
    row.appendChild(cell_3);
    table.appendChild(row);

    cell_1.appendChild(input_1);
    cell_2.appendChild(input_2);
    cell_3.appendChild(input_3);

    removeButton.textContent= "Remove_row";

    row.appendChild(removeCell);
    removeCell.appendChild(removeButton);

    removeButton.addEventListener("click", function(){
        removeButton.parentElement.parentElement.remove("td");
    });

});
