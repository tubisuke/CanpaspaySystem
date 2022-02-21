async function run() {
    let ranking = await eel.getRankingFromJavascript()();
    // alert(document.getElementById('first').innerHTML);
    document.getElementById('first').innerHTML = ranking[0][0] + ' (' +ranking[0][1] +'回)';
    document.getElementById('second').innerHTML = ranking[1][0] + ' (' +ranking[1][1] +'回)';
    document.getElementById('third').innerHTML = ranking[2][0] + ' (' +ranking[2][1] +'回)';
}
run();
