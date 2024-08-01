document.getElementById("open-redaction").addEventListener("click", function() {
    document.getElementById("redaction-modal-block").classList.add("open")
})

document.getElementById("close-redaction").addEventListener("click", function() {
    document.getElementById("redaction-modal-block").classList.remove("open")
})

document.getElementById("commit-redaction").addEventListener("click", function() {
    document.getElementById("redaction-modal-block").classList.remove("open")
})

window.addEventListener('keydown', (e) => {
    if(e.key === "Escape") {
        document.getElementById("redaction-modal-block").classList.remove("open")
    }
})