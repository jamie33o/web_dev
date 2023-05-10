
function blink() {
    var elem = document.querySelector(".table");
    elem.classList.toggle("hidden");
}

setInterval(blink, 500); // toggle the class every 500ms (half a second)

