// ================== EVENT LISTENERS ==================
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("login").addEventListener("click", Login);
    document.getElementById("buttonCadastrar").addEventListener("click", Cadastrar);
    document.getElementById("linkCadastro").addEventListener("click", toggleCadastro);
    document.getElementById("linkLogin").addEventListener("click", toggleCadastro);
});

// ================== LOGIN ==================
async function Login() {
    const email = document.getElementById("inputEmail").value;
    const senha = document.getElementById("inputPassword").value;

    if (!email || !senha) {
        alert("Preencha todos os campos!");
        return;
    }

    try {
        const resposta = await fetch("https://johnp3ter.pythonanywhere.com/login", {
            method: 'POST',
            headers: {'Content-Type':'application/json'},
            body: JSON.stringify({email, senha})
        });

        const dados = await resposta.json();

        if (resposta.ok) {
            localStorage.setItem("usuario_email", email);
            alert("Login Realizado com sucesso!");
        } else {
            alert(dados.erro || "Email ou senha incorretos.");
        }
    } catch (erro) {
        alert('Erro na conexão com o servidor.');
        console.error(erro);
    }
}

// ================== Cadastrar ==================
async function Cadastrar() {
    const url = "https://johnp3ter.pythonanywhere.com/cadastro";
    const cadastroForm = document.getElementById("caixaCadastro");

    const email = cadastroForm.querySelector('input[placeholder="Email"]').value;
    const senha = cadastroForm.querySelector('input[placeholder="Senha"]').value;

    try {
        const resposta = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, senha })
        });

        const dados = await resposta.json();

        if (resposta.ok) {
            localStorage.setItem("usuario_email", email);
            alert("Cadastro realizado com sucesso!");
        } else {
            alert(dados.erro || "Erro no cadastro.");
        }
    } catch (erro) {
        alert('Erro na conexão com o servidor.');
        console.error(erro);
    }
}

// ================== TOGGLE LOGIN / CADASTRO ==================
function toggleCadastro() {
    const loginDiv = document.getElementById("caixaLogin");
    const cadastroDiv = document.getElementById("caixaCadastro");
    loginDiv.classList.toggle("ativa");
    cadastroDiv.classList.toggle("ativa");
}
