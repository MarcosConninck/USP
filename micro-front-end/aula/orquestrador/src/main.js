import './style.css'

const rotas = [
    {
        path: '/',
        source: 'http://localhost:8002/',
        nome: 'Home',
    },
    {
        path: '/produtos',
        source: 'http://localhost:8003/',
        nome: 'Produtos',
    },
    {
        path: '/clientes',
        source: 'http://localhost:8001/',
        nome: 'Clientes',
    },
]

const navIframe = document.querySelector('#mf-nav')
const containerIframe = document.querySelector('#container')

const pathAtual = window.location.pathname

const mfInicial = rotas.find(r => r.path == pathAtual)
if (mfInicial) {
    containerIframe.setAttribute('src', mfInicial.source)

}

navIframe.onload = () => {
    navIframe.contentWindow.postMessage({ type: 'INICIAR', rotas: rotas }, 'http://localhost:8000/')
}

window.addEventListener('message', (evento) => {
    if (evento.data.type == 'NAVEGACAO') {
        console.log('HORA DE NAVEGAR PARA', evento.data.destino)
        const mfAlvoNavegacao = rotas.find(r => r.path == evento.data.destino.path)
        if (mfAlvoNavegacao) {
            containerIframe.setAttribute('src', mfAlvoNavegacao.source)
            window.history.pushState({}, '', mfAlvoNavegacao.path)
        }
    }
})

console.log(navIframe)

