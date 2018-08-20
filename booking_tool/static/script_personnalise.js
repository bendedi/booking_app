function updateNumber(nbPersonne) {
    toShow= document.getElementById("showNumber");
    toShow.innerHTML=nbPersonne
}
function hiddeDayTime() {
    containerHidding= document.getElementById("toshow")
    containerHidding.innerHTML= ""
    //containerStyle= document.getElementById("sub")
    //containerStyle.style.marginTop = "10vh";
}

function showDayTime() {
    var user = 1 ;
    containerShow= document.getElementById("toshow")
    containerShow.innerHTML= `<div class="form-check">
                <input class="plage" type="radio" name="exampleRadios1">
                <label class="form-check-label" for="exampleRadios2">
                Morning
                </label>
                </div>
                <div class="form-check">
                <input class="form-check-input" type="radio" name="exampleRadios1" >
                <label class="form-check-label" for="exampleRadios2">
                Afternoon
                </label>
                </div>
                <div class="form-check">
                <input class="form-check-input" type="radio" name="exampleRadios1" >
                <label class="form-check-label" for="exampleRadios2">
                Whatever
                </label>
                </div>`
    //containerStyle= document.getElementById("sub")
    //containerStyle.style.marginTop = "0%";
}