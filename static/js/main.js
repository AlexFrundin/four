var test = document.getElementById('id_city')
var country = document.getElementById('id_country')

test.onchange=function(){
  console.log("onchange")
}

test.onfocus=function(){
  if (test.length === 0){
    helpCity("Выберите страну")
    return
  }
  helpCity("")
  console.log("focus")
}

window.onload = function(){
  var block = document.getElementById('id_country')
  var info = Array.from(data.keys())
  var html = result(info)
  block.innerHTML = html
}

country.onchange=function(){
  name = document.getElementById('id_country').value
  var block = document.getElementById('id_city')
  if(name === ''){
    console.log("Empty")
    block.innerHTML = ''
    helpCity("Выберите страну")
    return
  }
  helpCity("Выберите город")

  city = data.get(name)
  var html = result(city)
  block.innerHTML = html
}

function result(info){
  var html = "<select>"
  html += "<option value=''></option>";
  for(var value of info){
    html+="<option value="+value+">"+value+"</option>"
  }
  html += "</select>"
  return html
}

function helpCity(txt){
  let info = document.getElementById("help_city")
  info.innerHTML = txt
}
