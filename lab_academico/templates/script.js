document.querySelector("form").addEventListener("submit", function (e) {
    e.preventDefault();
    const usuario = document.getElementById("usuario").value;
    const senha = document.getElementById("senha").value;
  
    if (usuario === "admin" && senha === "admin") {
      alert("Login bem-sucedido!");
    } else {
      alert("Usuário ou senha incorretos!");
    }
  });

  function openModal() {
    document.getElementById("modal").style.display = "flex";
  }
  
  function closeModal() {
    document.getElementById("modal").style.display = "none";
  }
  
  