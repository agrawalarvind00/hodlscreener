function rightScroll() {
    var container = document.getElementById('scroll');
    sideScroll(container,'right',25,280,10);
};

function leftScroll() {
    var container = document.getElementById('scroll');
    sideScroll(container,'left',25,280,10);
};

function sideScroll(element,direction,speed,distance,step){
    scrollAmount = 0;
    var slideTimer = setInterval(function(){
        if(direction == 'left'){
            element.scrollLeft -= step;
        } else {
            element.scrollLeft += step;
        }
        scrollAmount += step;
        if(scrollAmount >= distance){
            window.clearInterval(slideTimer);
        }
    }, speed);
}

function generate_table() {
    var tabBody = document.getElementsByTagName("tbody")[0];

    for(var i=0;i<2;i++){
        var row = document.createElement("tr");
        for(var j=0;j<5;j++){
            var cell = document.createElement("td");
            var cellText = document.createTextNode(data[btc][currency][i][j]);
            cell.appendChild(cellText);
            row.appendChild(cell);
        }
        tabBody.appendChild(row);
    }
}

function change_table(){
    var tabBody = document.getElementsByTagName("tbody")[0];
    tabBody.innerHTML = "";
    currency = document.getElementById("currency").value;
    btc = document.getElementById("bitcoin").value;
    for(var i=0;i<2;i++){
        var row = document.createElement("tr");
        for(var j=0;j<5;j++){
            var cell = document.createElement("td");
            var cellText = document.createTextNode(data[btc][currency][i][j]);
            cell.appendChild(cellText);
            row.appendChild(cell);
        }
        tabBody.appendChild(row);
    }
}