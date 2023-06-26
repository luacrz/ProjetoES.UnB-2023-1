from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dados fictícios
usuarios = [
    {"username": "professor", "password": "123", "tipo": "professor"},
    {"username": "aluno", "password": "456", "tipo": "aluno"}
]

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Verifica se o usuário existe e a senha está correta
        for usuario in usuarios:
            if usuario["username"] == username and usuario["password"] == password:
                # Redireciona para a página correspondente ao tipo de usuário
                if usuario["tipo"] == "professor":
                    return redirect("/professor")
                elif usuario["tipo"] == "aluno":
                    return redirect("/aluno")

        # Se o usuário não for encontrado, exibe uma mensagem de erro
        error_message = "Usuário ou senha inválidos. Tente novamente."
        return render_template("login.html", error_message=error_message)

    return render_template("login.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        tipo = request.form.get("tipo")

        # Adiciona o novo usuário aos dados fictícios
        usuarios.append({"username": username, "password": password, "tipo": tipo})

        # Redireciona para a página de login após o cadastro
        return redirect("/")

    return render_template("cadastro.html")

@app.route("/professor")
def professor():
    return "Página do professor"

@app.route("/aluno")
def aluno():
    return "Página do aluno"

if __name__ == "__main__":
    app.run(debug=True)
