// 参考：https://www.inmyzakki.com/entry/2018/02/21/172202

function getNextPage() {
    // ここでPython側の処理を実行
    // window.location.href = "../html/loading.html"; //ローディング画面への遷移
    eel.getNextPageFromJavascript();
}

eel.expose(signUpFromPython);
function signUpFromPython() {
    // 新規登録画面へジャンプする
    window.location.href = "../html/signUp.html";
}

eel.expose(mainPageFromPython);
function mainPageFromPython(){

    // メインページへの移動
    window.location.href = "../html/mainPage.html";
}
