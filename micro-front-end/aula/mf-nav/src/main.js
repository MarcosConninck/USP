const listaDeLinks = document.querySelector('#lista-de-links')

window.addEventListener('message', (evento) => {
    if (evento.data.type == 'INICIAR') {
        // console.log(evento.data)
        evento.data.rotas.forEach(element => {
            console.log(element)
            const li = document.createElement('li')
            const ancora = document.createElement('a')
            ancora.innerHTML = element.nome
            ancora.setAttribute('href', element.path)

            ancora.addEventListener('click', (evt) => {
                evt.preventDefault()
                window.parent.postMessage({ type: 'NAVEGACAO', destino: rotas }, '*')
            })

            li.appendChild(ancora)
            listaDeLinks.appendChild(li)
        });
    }
})