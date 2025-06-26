from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# Suas listas globais
pratos = []
usuarios = []

# Página inicial
@app.route('/')
def home():
    return render_template('home.html')  # Aqui carrega sua página inicial

# Página do cardápio
@app.route('/cardapio')
def cardapio():
    return render_template('index.html', pratos=pratos)

# Página para adicionar prato
@app.route('/prato_novo', methods=['GET', 'POST'])
def prato_novo():
    if request.method == 'POST':
        nome = request.form['nome']
        ingredientes = request.form['ingredientes']
        preco = float(request.form['preco'])
        pratos.append({'nome': nome, 'ingredientes': ingredientes, 'preco': preco})
        return redirect('/cardapio')
    return render_template('novo_prato.html')

# Página para ver usuários
@app.route('/usuarios')
def ver_usuarios():
    return render_template('usuarios.html', usuarios=usuarios)

# Página para adicionar usuário
@app.route('/novo_usuario', methods=['GET', 'POST'])
def novo_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        tel = request.form['tel']
        usuarios.append({'nome': nome, 'endereco': endereco, 'tel': tel})
        return redirect('/usuarios')
    return render_template('novo_usuario.html')

# Rodar app
if __name__ == '__main__':
    app.run(debug=True)