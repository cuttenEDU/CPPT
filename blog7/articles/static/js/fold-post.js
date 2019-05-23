var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function (event) {
        if (event.target.parentElement.parentElement.parentElement.className == "one-post folded") {
            event.target.innerHTML = "cвернуть";
            event.target.parentElement.parentElement.parentElement.className = "one-post"
        } else {
            event.target.innerHTML = "развернуть";
            event.target.parentElement.parentElement.parentElement.className = "one-post folded"
        }
    });
}