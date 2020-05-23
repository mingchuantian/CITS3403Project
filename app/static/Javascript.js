
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

    xhttp.open ("GET", "/API", true);
    xhttp.send();

}

function myFunc (xml) {

    let x0 = xml.responseText;

    let t1 = "<tr> <th> Student Name </th> <th> Quiz_taken Times </th> </tr>";

    // let x0 = JSON.parse(xmlDoc);

    console.log(x0);             

    x0.map(

        function (x0) {
            t1 += "<tr> <td>" 
                + x.name + "</td> <td>" 
                + x.Quiz_taken + "</td> </tr>";
        }
    )

    document.getElementById("myJSON").innerHTML = t1;

}