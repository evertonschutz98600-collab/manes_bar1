from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Banco de dados simulado em memória (Cardápio Completo do Arena Bugiganga)
cardapio_db = [
    {
        "id": 1,
        "categoria": "Lanches",
        "nome": "X-Bugiganga Especial",
        "descricao": "Pão brioche, carne artesanal 160g, queijo cheddar derretido, bacon crocante, alface e molho especial.",
        "preco": 32.00,
        "foto": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80",
        "adicionais": [
            {"nome": "Bacon Extra", "preco": 5.00},
            {"nome": "Ovo Frito", "preco": 3.00},
            {"nome": "Dobro de Carne", "preco": 10.00},
            {"nome": "Cheddar Cremoso", "preco": 4.00}
        ]
    },
    {
        "id": 2,
        "categoria": "Lanches",
        "nome": "X-Burger Simples",
        "descricao": "Pão com gergelim, carne 120g, queijo prato, maionese verde e alface.",
        "preco": 22.00,
        "foto": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=600&q=80",
        "adicionais": [
            {"nome": "Bacon Extra", "preco": 5.00},
            {"nome": "Ovo Frito", "preco": 3.00},
            {"nome": "Queijo Extra", "preco": 4.00}
        ]
    },
    {
        "id": 3,
        "categoria": "Porções",
        "nome": "Porção de Batata Frita com Bacon e Cheddar (G)",
        "descricao": "Batatas fritas sequinhas e crocantes cobertas com muito cheddar cremoso e bacon em cubos.",
        "preco": 38.00,
        "foto": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&w=600&q=80",
        "adicionais": [
            {"nome": "Extra Cheddar", "preco": 6.00},
            {"nome": "Extra Bacon", "preco": 6.00}
        ]
    },
    {
        "id": 4,
        "categoria": "Porções",
        "nome": "Frango a Passarinho Crocante",
        "descricao": "Porção suculenta temperada com alho e ervas finas, acompanhada de limão e molho tártaro.",
        "preco": 42.00,
        "foto": "https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58?auto=format&fit=crop&w=600&q=80",
        "adicionais": [
            {"nome": "Molho Especial da Casa", "preco": 3.50}
        ]
    },
    {
        "id": 5,
        "categoria": "Bebidas",
        "nome": "Coca-Cola Lata 350ml",
        "descricao": "Gelada.",
        "preco": 6.00,
        "foto": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?auto=format&fit=crop&w=600&q=80",
        "adicionais": []
    },
    {
        "id": 6,
        "categoria": "Bebidas",
        "nome": "Suco Natural de Laranja 500ml",
        "descricao": "Feito na hora com frutas frescas.",
        "preco": 8.00,
        "foto": "https://images.unsplash.com/photo-1613478223719-2ab802602423?auto=format&fit=crop&w=600&q=80",
        "adicionais": []
    }
]

@app.route('/')
def index():
    return render_template('cardapio.html', cardapio=cardapio_db)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)