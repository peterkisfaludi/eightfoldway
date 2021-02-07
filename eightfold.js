<!DOCTYPE html>
<html>
<head>
<style>
table, td {
  border: 1px solid black;
}
</style>
</head>
<body onload="genBoard()">

<table id="board">
</table>

<button onclick="rotator()">Rotate</button>

<script>

var R=8;
var C=8;
var placement_state=1;
var rot_state=true;
var A = new Array(R); 
for (var i = 0; i < A.length; i++) { 
    A[i] = Array(C); 
} 
for (var i = 0; i < R; i++) { 
    for (var j = 0; j < C; j++) { 
        A[i][j] = 0; 
    } 
}
var hilited=[];

function rotator(){
  rot_state=!rot_state;
 }

function canHilite(y,x, length){
  var ret = (A[y][x]==0);      
  for(var i=0;i<length;i++){
    if(rot_state==true){
      if(y+i>=R){return false;}
      ret=ret && A[y+i][x]==0;
    } else {
      if(x+i>=C){return false;}
      ret=ret && A[y][x+i]==0;
    }
  }
  return ret;
}

function setColor(y,x,color){
  document.getElementById('board').rows[y].cells[x].style.backgroundColor = color;
}

function doHilite(y,x){
  var hiliColor = "#FF0000";
  setColor(y,x,hiliColor);
  hilited.push([y,x]);
}

function undoHilite(){
  var normalColor = "#FFFFFF";
  for(var i=0;i<hilited.length;i++){
    setColor(hilited[i][0],hilited[i][1],normalColor);  
  }
  hilited=[];
}


function mouseOver(cell) {
  var x=cell.cellIndex;
  var y=cell.parentNode.rowIndex;

  switch(placement_state) {
    case 1:
      if(canHilite(y,x,1)){
        doHilite(y,x);
      }      
      break;
    case 2:      
      if(canHilite(y,x,2)){
        doHilite(y,x);
        if(rot_state==true){
          doHilite(y+1,x);
        } else {
          doHilite(y,x+1);
        }
      }            
      break;
    case 3:      
      if(canHilite(y,x,3)){
        doHilite(y,x);
        if(rot_state==true){
          doHilite(y+1,x);
          doHilite(y+2,x);
        } else {
          doHilite(y,x+1);
          doHilite(y,x+2);
        }
      }            
      break;


default:
    // code block
  }

}
function mouseOut(cell) {
  var x=cell.cellIndex;
  var y=cell.parentNode.rowIndex;
  undoHilite();
}

function markOccupied(y,x){
  document.getElementById('board').rows[y].cells[x].innerHTML = "X";
  A[y][x]=1;
  rot_state=false;
}

function mouseClick(cell) {
  var x=cell.cellIndex;
  var y=cell.parentNode.rowIndex;
  for(var i=0;i<hilited.length;i++){
  	markOccupied(hilited[i][0],hilited[i][1]);
  }
  if(hilited.length>0){
  	undoHilite();
    placement_state+=1;
    if(placement_state==4){
    	alert('solving');
    }
  }
  
}

function genBoard() {
  var brdTxt="";
  for(var i=0;i<8;i++){
    brdTxt+="<tr>";
  	for(var j=0;j<8;j++){
  	  brdTxt+="<td onmouseover=\"mouseOver(this)\" onclick=\"mouseClick(this)\" onmouseout=\"mouseOut(this)\">hello</td>";      
    }
    brdTxt+="</tr>";
  }
  document.getElementById("board").innerHTML = brdTxt;
  
  
}
</script>

</body>
</html>
