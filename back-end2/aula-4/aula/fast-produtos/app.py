from fastapi import FastAPI
from models.produto import Product

data = [
    Product(id=1, name="Tenis", description="Calçados", price=200),
    Product(id=2, name="Camiseta", description="Roupa", price=50),
    Product(id=3, name="Notebook", description="Eletrônicos", price=3000),
]

app = FastAPI()


@app.get("/")
def say_hello():
    return {"FastAPI": "Hello"}


@app.get("/api/product")
def get_products():
    """Pega todos os produtos"""
    return data


@app.get("/api/product/{id}")
def get_product_by_id(id: int):
    """Pega produto um a um"""
    for product in data:
        if product.id == id:
            return product
    return {"message": "Nenhum produto encontrado com o ID fornecido"}


# @app.get("/{name}")
# def say_hi(name: str):
#     return {"Hello": name}
