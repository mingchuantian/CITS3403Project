
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


async function getAPI(quizID){

    console.log(quizID)
    const url = "/API/";
    url.concat(String(quizID))
    console.log(url)

    fetch(url)
        .then((resp) => resp.json())
        .then(
            function(data){
                console.log(data)

                const container = document.getElementById("myJSON")
                var t2 = document.createElement("p")
                var t2content = document.createTextNode(data)
                t2.appendChild(t2content)
                container.appendChild(t2)


            }
            
        )

}

/*  check the new quiz finished or not */
function submit_new_quiz(){
    if(document.getElementsByClassName("quiz").length > 0){ //  if quiz creating not finished, alert
        alert('The quiz creating is not finished already, you can not submit it!');
    }else{
        alert('you finished all the quiz question creating!');  //  if finished already, alert and back to the teacher page
        window.open("/user","_self");
    }
}


/*  click it to check the student finished or not*/
function submit_quiz_answer(){
    if(document.getElementsByClassName("quiz").length > 0){ //  if still quiz there, not finished
        alert('You did not finish all questions, please do not submit it!');    //  alert this
    }else{
        alert('you finished all the quiz question, now submit it!');    //  if finished, alert it
        document.getElementById('finishthis').click();  //  submit it
    }
}

/*  back to the user page */
function back_teacher_page(){
    window.open("/user","_self");
}

function back_student_page(){
    window.open("/user","_self");
}


function loadPage(){
    var target = document.getElementById('url').value;
    console.log(target);
    document.getElementById('iframePosition').src = target;
}

function timer_reset(){     //  reset the timer when the user click the "finish" button in the student quiz page
    window.name = '';
    clearInterval(timer);
}