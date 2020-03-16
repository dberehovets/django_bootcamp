var fPlayer = prompt("Who is first player?")
var sPlayer = prompt("Who is second player?")

$('#turn').text(fPlayer + ": it is your turn, please pick a column to drop your blue chip.")
buttons = $('button')
var color = '#4285F4'
var user = fPlayer

function changeColor(){
  if (color == '#4285F4'){
    color = "#DB4437"
  }else {
    color = '#4285F4'
  }
}

function changeTurn(){
  if (user == fPlayer){
    user = sPlayer
    $('#turn').text(user + ": it is your turn, please pick a column to drop your red chip.")
  }else {
    user = fPlayer
    $('#turn').text(user + ": it is your turn, please pick a column to drop your blue chip.")
  }
}

function paintButton(){
  this.style.background = color
  changeColor()
  changeTurn()
  this.disabled = true
}

function clicked(){
  if (!this.disabled){
    index = buttons.index(this)

  }
}

for (button of buttons){
  button.addEventListener('click', clicked)
}
