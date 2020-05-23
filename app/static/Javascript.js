
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


    let xmlDoc = xml.responseText;

    let t1 = "<tr> <th> Student Name </th> <th> Quiz_taken Times </th> </tr>";
    

    let x0 = JSON.parse(xmlDoc);

    console.log(x0);  
    console.log(x0.name);        

    //t1 = "<p>" + x0.ID + "</p>"

    /*
    x0.map(

        function (x0) {
            t1 += "<tr> <td>" 
                + x.name + "</td> <td>" 
                + x.Quiz_taken + "</td> </tr>";
        }
    )
    */
   const container = document.getElementById("myJSON")
   var t2 = document.createElement("p")
   var t2content = document.createTextNode(x0)
   t2.appendChild(t2content)
    container.appendChild(t2)

}


async function getAPI(){

    const url = "http://localhost:5000/API"

    fetch(url)
        .then((resp) => resp.json())
        .then(
            function(data){
                console.log(data)
                console.log(data.name)

                let names = data.name;

                return names.map(
                    function(names){
                        const container = document.getElementById("myJSON")
                        var t2 = document.createElement("p")
                        var t2content = document.createTextNode(data.name)
                        t2.appendChild(t2content)
                         container.appendChild(t2)
                    }
                )
            }
            
        )

}