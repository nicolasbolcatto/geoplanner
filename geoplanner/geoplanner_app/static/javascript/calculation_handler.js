document.addEventListener("DOMContentLoaded", () => {

  run_calculation()


    document.getElementById("calculate").onclick = function() {
      run_calculation()
    }

})

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

function run_calculation(){

  coords_count = document.querySelectorAll('.coords_count').length;
  coordinates = []

  document.querySelectorAll('.coords_count').forEach(row => {
      id = row.id
      lat = parseFloat(document.getElementById("lat"+id).value)
      long = parseFloat(document.getElementById("long"+id).value)
      coordinates.push(
          [lat, long]
      )      
  })

  console.log(coordinates)


  fetch(`/calculate`,
  {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      "X-CSRFToken": getCookie("csrftoken")              
    },
    method: "POST",
    body: JSON.stringify({'coordinates':coordinates})
  })
  .then(response => response.json())
  .then(data => {
      console.log('success')
      base64_plot = data["json_display"]
      document.getElementById("results_plot").src = "data:image/png;base64," + base64_plot;

      document.getElementById("result1").innerHTML = data["result1"]
      document.getElementById("result2").innerHTML = data["result2"]
      document.getElementById("result3").innerHTML = data["result3"]
      document.getElementById("result4").innerHTML = data["result4"]


      })
}