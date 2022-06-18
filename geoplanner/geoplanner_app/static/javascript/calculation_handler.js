document.addEventListener("DOMContentLoaded", () => {



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

  project_class = document.getElementById("project-class").value
  soil_class = document.getElementById("soil-class").value

  /* THIS IS FOR GETTING ELEMENTS FROM THE COORDINATE TABLE
  document.querySelectorAll('.coords_count').forEach(row => {
      id = row.id
      lat = parseFloat(document.getElementById("lat"+id).value)
      long = parseFloat(document.getElementById("long"+id).value)
      coordinates.push(
          [lat, long]
      )      
  })
  */

  console.log(draw.Zv.length)
  coord_holder = []

  for (var i = 0; i < draw.Zv.length; i++) {
    coord_holder.push(convert3857to4236(draw.Zv[i][1], draw.Zv[i][0]))
  }

  coordinates = coord_holder

  fetch(`/calculate`,
  {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      "X-CSRFToken": getCookie("csrftoken")              
    },
    method: "POST",
    body: JSON.stringify({'coordinates':coordinates,'project_class':project_class, 'soil_class':soil_class})
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


      xs = data["xs"]
      ys = data["ys"]

      for (var i = 0; i < xs.length; i++) {
        var marker = new ol.Feature(new ol.geom.Point(ol.proj.fromLonLat([xs[i], ys[i]])));
        markers.getSource().addFeature(marker);
      }


      })
}


function convert3857to4236(lat3857, long3857){
    const e = 2.7182818284
    const X = 20037508.34

    
    //converting the logitute from epsg 3857 to 4326
    var long4326 = (long3857*180)/X
    
    //converting the latitude from epsg 3857 to 4326 split in multiple lines for readability
    
    let lat4326 = lat3857/(X / 180)
    var exponent = (Math.PI / 180) * lat4326
    
    lat4326 = Math.atan(e ** exponent)
    lat4326 = lat4326 / (Math.PI / 360)
    lat4326 = lat4326 - 90

    return [long4326, lat4326]
}