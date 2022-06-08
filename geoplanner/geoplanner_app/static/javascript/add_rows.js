// based on https://engineertodeveloper.com/dynamic-formsets-with-django/
// javascript script to ad rows to formsets
document.addEventListener("DOMContentLoaded", () => {

  listen_delete()

  document.getElementById("add").onclick = function() {
    count = document.querySelectorAll('.coords_count').length;
    count++;
    var objTo = document.getElementById('coords_table_body');
    var divtest = document.createElement("tr");
    divtest.classList.add("coords_count");      
    divtest.setAttribute("id", count);        
    divtest.innerHTML = '<th scope="row">'+count+'</th><td><input type="number" id="lat'+count+'" class="form-control" value="51.4934"></td><td><input type="number" id="long'+count+'" class="form-control" value="0.0098"></td><td><button data-id="'+count+'" class="align-self-center btn btn-danger delete_coord" style="padding:1px 8px">X</button></td>';
    objTo.appendChild(divtest)
    listen_delete()
  }


});

function listen_delete(){
  document.querySelectorAll('.delete_coord').forEach(button => {
    button.onclick = function() {
      selected=button.getAttribute('data-id')
      console.log(selected)

      let node = document.getElementById(selected);
      if (node.parentNode) {
        node.parentNode.removeChild(node);
        }
      else {
        return
      }      



    }
  })
}