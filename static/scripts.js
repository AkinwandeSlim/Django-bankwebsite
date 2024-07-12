document.addEventListener('DOMContentLoaded', function () {

    const images = document.getElementsByClassName("plusimg")
    const buttons = document.getElementsByClassName("accordion-btn");
    const items = document.getElementsByClassName("accordion-itm")

    for (let i = 0; i < buttons.length; i++) {
      buttons[i].addEventListener("click", function () {
        const targetId = buttons[i].getAttribute("data-target");
        const hiddenBody = document.getElementById(targetId);
        

        if (hiddenBody.classList.contains("hidden")) {
            images[i].src = "img\icon-green-minus.svg";
            hiddenBody.classList.remove("hidden");
            items[i].classList.add("open");

        } else if (!hiddenBody.classList.contains("hidden")){
            images[i].src = "img\icon-green-plus.svg"
            hiddenBody.classList.add("hidden"); 
            items[i].classList.remove("open")
        }   
      });
    }
});
