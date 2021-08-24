function rightScroll() {
    var container = document.getElementById('scroll');
    sideScroll(container,'right',25,270,10);
};

function leftScroll() {
    var container = document.getElementById('scroll');
    sideScroll(container,'left',25,270,10);
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