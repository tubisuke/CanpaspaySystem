// 参考：https://sounansa.net/archives/647

var button = document.querySelector("#login")
button.addEventListener("submit", signUpAction);

function signUpAction() {

    var userID = document.querySelector("#userID").value;
    var password = document.querySelector("#password").value;

    // alert(userID);
    // var userID = document.login.userID.value;
    // var password = document.login.pass.value;

    eel.signUpFromJavascript(userID,password);
}

eel.expose(mainPageFromPython);
function mainPageFromPython(){

    // メインページへの移動
    window.location.href = "../html/mainPage.html";
}
