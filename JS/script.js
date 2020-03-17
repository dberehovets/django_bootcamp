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

function paintButton(button){
  button.style.background = color
  changeColor()
  changeTurn()
  button.disabled = true
}

function checkWinner(){
  rows = $('tr')
  for (row of rows){
    cells = row.cells
    check_color = 'grey'
    count = 0
    for (cell of cells){
      button = cell.querySelector('button')
      if (button.disabled){
        btColor = button.style.background
        if (btColor == check_color){
          count++
        }else if (btColor == "rgb(219, 68, 55)") {
          check_color = "rgb(219, 68, 55)"
          count = 1
        }else if(btColor == 'rgb(66, 133, 244)'){
          check_color = 'rgb(66, 133, 244)'
          count = 1
        }
      }
      if (count >= 4){
        if (check_color == 'rgb(66, 133, 244)'){
          $('h1').text(fPlayer + " winner! Refresh the page to play again!")
          $('h2').text("...")
          $('h3').text("...")
        } else if (check_color == "rgb(219, 68, 55)"){
          $('h1').text(sPlayer + " winner! Refresh the page to play again!")
          $('h2').text("...")
          $('h3').text("...")
        }
        for (button of buttons){
          button.disabled = true
        }
        break
      }
      }
  }
}

function clicked(){
  if (!this.disabled){
    index = buttons.index(this)
    rows = $('tr')
    for (var i=5; i>=0; i--){
      button = rows[i].cells[index % 7].querySelector('button')
      if (!button.disabled){
        paintButton(button)
        break
      }
    }
  }
  checkWinner()
}

for (button of buttons){
  button.addEventListener('click', clicked)
}
