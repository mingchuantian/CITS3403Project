
// When the user clicks on the button, scroll to the top of the document
function toTopFunc() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

// Using AJAX to show the student who has taken the quiz and the times of taking quiz
function loadDoc () {

    let xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        myFunc(this);
    };

    xhttp.open ("GET", "/students_taken", true);
    xhttp.send();

}

function myFunc (xml) {

    let xmlDoc = xml.responseText;

    let t1 = "<tr> <th> Student </th> <th> Times of taking quiz </th> </tr>";

    let x0 = JSON.parse(xmlDoc);

    console.log(x0);

    // let x = x0.locations;              

    // x.map(

    //     function (x) {
    //         t1 += "<tr> <td>" 
    //             + x.country + "</td> <td>" 
    //             + x.latest.confirmed + "</td> <td>" 
    //             + x.latest.deaths + "</td> </tr>";
    //     }
    // )

    document.getElementById("myJSON").innerHTML = x0;

}