from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

usuarios = {
    "joao@gmail.com": {"senha": "12345678"},
    "maria@gmail.com": {"senha": "12345678"}
}

@app.route('/', methods=["GET"])
def index():
    return "API funcionando"

@app.route('/usuarios', methods=["GET", "OPTIONS"])
def obter_usuarios():
    if request.method == "OPTIONS":
        resp = make_response("", 200)
        resp.headers["Access-Control-Allow-Origin"] = "*"
        resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
        resp.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        return resp

    resp = jsonify(usuarios)
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

@app.route('/login', methods=["POST", "OPTIONS"])
def login():
    if request.method == "OPTIONS":
        resp = make_response("", 200)
        resp.headers["Access-Control-Allow-Origin"] = "*"
        resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
        resp.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        return resp

    dados = request.get_json(silent=True) or {}
    email = dados.get("email")
    senha = dados.get("senha")

    if email in usuarios and usuarios[email]["senha"] == senha:
        resp = jsonify({"mensagem": "login realizado com sucesso!"})
        resp.status_code = 200
        resp.headers["Access-Control-Allow-Origin"] = "*"
        return resp

    resp = jsonify({"erro": "email ou senha inválidos"})
    resp.status_code = 401
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

@app.route('/cadastro', methods=["POST", "OPTIONS"])
def cadastro():
    if request.method == "OPTIONS":
        resp = make_response("", 200)
        resp.headers["Access-Control-Allow-Origin"] = "*"
        resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
        resp.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        return resp

    dados = request.get_json(silent=True) or {}
    email = dados.get("email")
    senha = dados.get("senha")

    if not email or not senha:
        resp = jsonify({"erro": "Preencha email e senha"})
        resp.status_code = 400
        resp.headers["Access-Control-Allow-Origin"] = "*"
        return resp

    if email in usuarios:
        resp = jsonify({"erro": "Email já cadastrado"})
        resp.status_code = 409
        resp.headers["Access-Control-Allow-Origin"] = "*"
        return resp

    usuarios[email] = {"senha": senha}

    resp = jsonify({"mensagem": "Usuário cadastrado com sucesso!"})
    resp.status_code = 201
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp