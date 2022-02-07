
var login = 0;
var login_alert = false;

var name_ = localStorage.getItem("name");
var password = localStorage.getItem("password");

// setInterval (() => {
    name_ = localStorage.getItem("name");
    password = localStorage.getItem("password");

    if (name_ == null) {
        login = 0;
        login_alert = true;
        document.getElementById('s1').style.display = 'flex';
        document.getElementById('s2').style.display = 'none';
        document.getElementById('s3').style.display = 'none';
    }
    else {
        if (password == null) {
            login = 0;
            login_alert = true;
            document.getElementById('s1').style.display = 'flex';
            document.getElementById('s2').style.display = 'none';
            document.getElementById('s3').style.display = 'none';
        }
        else {
            login = 1;
            login_alert = false;
            document.getElementById('lt').innerText = name_;
            document.getElementById('s1').style.display = 'none';
            document.querySelector('.s12').style.display = 'none';
            document.getElementById('s2').style.display = 'flex';
            document.getElementById('s3').style.display = 'flex';
        }
    }
// }, 1000);