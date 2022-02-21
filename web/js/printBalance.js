// 参考：https://github.hubspot.com/odometer/docs/welcome/#2
// 参考：http://temping-amagramer.blogspot.com/2015/03/javascript-odometer.html

// odometerOptions = { auto: false }; // Disables auto-initialization
//
// // For each odometer, initialize with the theme passed in:
// var odometer = new Odometer({ el: $('.odometer')[0], value: 123, theme: 'car' });
// odometer.render();

setTimeout(function(){
    // alert("Hello");
    async function run() {
        let balance = await eel.getBalanceFromJavascript()();
        // alert(balance);
        odometer.innerHTML = balance;

    }
    run();
    // console.log(balance)
}, 1000);
