function validasiLogin(){
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    
    if (username == "ahmad2017") {
        if (password == "integrity"){
            window.location.href = "berhasilLogin.html"
            alert("Login berhasil!")
        } else {
            alert("Password yang anda masukan salah");
        }
    } else {
        alert("Username yang anda masukan salah");
    }
}