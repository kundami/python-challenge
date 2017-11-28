
/* global Plotly */
var queryURL ="http://127.0.0.1:5000/names";

/* d3.json(queryURL, function(error, response) {
//       if (error) return console.warn(error);

//       console.log(response);
//  })
*/

function renderList(){
var list = document.getElementById('selDataset');
console.log("starting render") ;
console.log(belly_bacteria_names) ;
list.innerHTML = "";
belly_bacteria_names.forEach(function(item){
   var option = document.createElement('option');
   option.value = item;
   console.log(item) ;
   list.appendChild(option);
});
}

renderList();
/**
 * Helper function to select stock data
 * Returns an array of values
 * @param {array} rows
 * @param {integer} index
 * index 0 - Date
 * index 1 - Open
 * index 2 - High
 * index 3 - Low
 * index 4 - Volume
 */
