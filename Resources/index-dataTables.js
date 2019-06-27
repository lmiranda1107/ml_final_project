// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");

// Set filteredBCdata to dataSet initially
var filteredBCdata= dataSet; 

// renderTable renders the filterdata to the tbody
function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < filteredBCdata.length; i++) {
    // Get get the current patient object and its fields
    var patient = filteredBCdata[i];
    var observations = Object.keys(patient);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < observations.length; j++) {
      // For every observations in the ufo object, create a new cell at set its inner text to be the current value at the current     ufo'sobservation
      var observation = observations[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = patient[observation];
    }
  }
}



// Render the table for the first time on page load
renderTable();
