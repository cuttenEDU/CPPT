var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function (event) {
        if (event.target.parentElement.parentElement.className === "one-post folded") {
            event.target.innerHTML = "Cвернуть";
            event.target.parentElement.parentElement.className = "one-post"
        } else {
            event.target.innerHTML = "Развернуть";
            event.target.parentElement.parentElement.className = "one-post folded"

        }
    });
}