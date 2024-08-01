document.getElementById("open-filters").addEventListener("click", function() {
    document.getElementById("filter-modal-block").classList.add("open")
})

document.getElementById("open-quation").addEventListener("click", function() {
    document.getElementById("quation-modal-block").classList.add("open")
})

//5
document.getElementById("close-filters").addEventListener("click", function() {
    document.getElementById("filter-modal-block").classList.remove("open")
})

document.getElementById("close-quation").addEventListener("click", function() {
    document.getElementById("quation-modal-block").classList.remove("open")
})

//4
document.getElementById("commit-filters").addEventListener("click", function() {
    document.getElementById("filter-modal-block").classList.remove("open")
})

document.getElementById("commit-quation").addEventListener("click", function() {
    document.getElementById("quation-modal-block").classList.remove("open")
})

//3
window.addEventListener('keydown', (e) => {
    if(e.key === "Escape") {
        document.getElementById("filter-modal-block").classList.remove("open")
    }
})

window.addEventListener('keydown', (e) => {
    if(e.key === "Escape") {
        document.getElementById("quation-modal-block").classList.remove("open")
    }
})

//2
document.querySelector("filter-modal-block .modal-box").addEventListener('click', event => {
    event._isClickWithInModal = true
})

document.querySelector("quation-modal-block .modal-box").addEventListener('click', event => {
    event._isClickWithInModal = true
})