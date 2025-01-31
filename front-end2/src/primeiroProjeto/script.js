let button = document.querySelector(".incremento")
let button2 = document.querySelector(".zerar")

button.addEventListener("click", somaUm)

function somaUm() {
    let contador = document.querySelector("h3")
    let valorH3 = parseInt(contador.textContent)
    let novoValor = valorH3 + 1
    contador.textContent = novoValor
    contador.style.color = "rgb(2,3,4)"
    
    let r = parseInt(Math.random() * 256)
    let g = parseInt(Math.random() * 256)
    let b = parseInt(Math.random() * 256)
    
    if (novoValor > valorH3) {
        contador.style.color = `rgb(${r}, ${g}, ${b})`
    } if (valorH3 == 9) {
        alert("viu como os botões trocam de cor? rs")
    }
}

button2.addEventListener("click", () => {
    let button2 = document.querySelector("h3")
    button2.textContent = 0
})
