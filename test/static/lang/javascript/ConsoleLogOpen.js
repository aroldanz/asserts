function functionAWithConsoleLog() {
    var a = 13
    var b = 31
    var c = Math.floor((Math.random() * 100) + 1);
    console.log()
    localStorage.getItem('key');
    try {
        if(a == "") throw "empty";
        if(isNaN(a)) throw "not a number";
        c = Number(a);
        if(c < 5) throw "too low";
        if(c > 10) throw "too high";
        eval('alert("Your query string was ' + unescape(document.location.search) + '");');
    }
    catch(err) {
    }

    switch (new Date().getDay()) {
        case 0:
            day = "Sunday";
            break;
        case 1:
            day = "Monday";
            break;
        case 2:
            day = "Tuesday";
            break;
        case 3:
            day = "Wednesday";
            break;
        case 4:
            day = "Thursday";
            break;
        case 5:
            day = "Friday";
            break;
        case 6:
            day = "Saturday";
    }
}

function functionBWithConsoleLog() {
    var a = 13
    var b = 31
    console.log(a+b)
    localStorage.clear();
    try {
        if(a == "") throw "empty";
        if(isNaN(a)) throw "not a number";
        c = Number(a);
        if(c < 5) throw "too low";
        if(c > 10) throw "too high";
    }
    catch(err) {
        //console.log(a+b)
    }

    try {
        if(b == "") throw "empty";
        if(isNaN(b)) throw "not a number";
        c = Number(b);
        if(c < 5) throw "too low";
        if(c > 10) throw "too high";
    }

    catch(err) {
        /*
        console.log(a+b)
        */
    }

    switch (new Date().getDay()) {
        case 0:
            day = "Sunday";
            break;
        case 1:
            day = "Monday";
            break;
        case 2:
            day = "Tuesday";
            break;
        case 3:
            day = "Wednesday";
            break;
        case 4:
            day = "Thursday";
            break;
        case 5:
            day = "Friday";
            break;
        case 6:
            day = "Saturday";
        //default:
            //day = "Error";
        /*default:
            day = "Error";
        */
    }
}