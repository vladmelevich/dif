document.getElementById("open-answer").addEventListener("click", function() {
    document.getElementById("answer-modal-block").classList.add("open")
})

document.getElementById("close-answer").addEventListener("click", function() {
    document.getElementById("answer-modal-block").classList.remove("open")
})

document.getElementById("commit-answer").addEventListener("click", function() {
    document.getElementById("answer-modal-block").classList.remove("open")
})

window.addEventListener('keydown', (e) => {
    if(e.key === "Escape") {
        document.getElementById("answer-modal-block").classList.remove("open")
    }
})

document.querySelector("answer-modal-block .modal-box").addEventListener('click', event => {
    event._isClickWithInModal = true
})