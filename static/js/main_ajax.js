var country = document.getElementById('id_country')
var form = document.getElementById('id_form')


country.onchange = function(event){
  document.getElementById('id_city').innerHTML=""
  let name_country = country.value
  if (name_country === ''){
    console.log("BAD")
    return}
  let info = $('#id_form').serialize()
  event.preventDefault()
  sendServer(info)
}

function sendServer(data){
  $.ajax({
    url: '',
    method: "POST",
    data : data,
    success: function(server_answer){
      console.log(server_answer.data)
      document.getElementById('id_city').innerHTML = result(server_answer.data)
    },
    error: function(xhr, errmsg, sms){
      $('#results').html(sms);
      // console.log(xhr);
      // console.log(errmsg);
      // console.log(err);
      }
  })
}


function result(info){
  var html = "<select>"
  html += "<option value=''></option>";
  for(var value of info){
    html+="<option value="+value[1]+">"+value[0]+"</option>"
  }
  html += "</select>"
  return html
}
