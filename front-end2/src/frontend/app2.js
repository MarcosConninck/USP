// let endpoint = './dados.json'
let products = []
let elementToInserProducts = document.getElementById("produtos__lista")
searchProducts()

async function searchProducts() { 
    let res = await fetch("./dados.json") // aguardar o que vai acontecer (se estiver local, escrever o diretorio, ao invés de chamar a api)
    products = await res.json();
    console.table(products);
    showProducts(products)
}

function showProducts(products) {
    products.forEach(product => {
        elementToInserProducts.innerHTML += 
        `<li class="produtos__item">
                    <div class="produtos__content">
                        <img src=${product.img} alt="Imagem de celular">
                        <div class="produtos__informacoes">
                            <h3>${product.nome}</h3>
                            <p>${product.descricao}
                            </p>
                            <h4>R$ ${product.valorComDesconto}<s>R$ ${product.valorSemDesconto}</s></h4>
                            <p>${product.tipoEntrega}</p>
                        </div>
                    </div>
                </li>`
    });
}