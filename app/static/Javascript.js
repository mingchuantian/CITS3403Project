
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

// Function that retrieves API
async function getAPI(){

    var url = "/API"

    fetch(url)
        .then((resp) => resp.json())
        .then(
            function(data){

                console.log(data)
                
                let t = "<tr> <th> Title </th> <th> Number of Questions </th><th> Questions </th><th> Number of Students </th> <th> Student Name </th></tr>";

                data.map(
                    function(data){

                        t += "<tr> <td>" 
                                + data.title + "</td> <td>" 
                                + data.Question_Number  + "</td> <td>" 
                                + data.questions  + "</td> <td>" 
                                + data.numStudents  + "</td> <td>" 
                                + data.student_names + "</td> </tr>";

                    }

                )
                
                document.getElementById("myJSON").innerHTML = t;

            }
            
        )

}

/*  check the new quiz finished or not */
function submit_new_quiz(){
    if(document.getElementsByClassName("quiz").length > 0){
        alert('The quiz creating is not finished already, you can not submit it!');
    }else{
        alert('you finished all the quiz question creating!');
        window.open("/user","_self");
    }
}


/*  click it to check the student finished or not*/
function submit_quiz_answer(){
    if(document.getElementsByClassName("quiz").length > 0){
        alert('You did not finish all questions, please do not submit it!');
    }else{
        alert('you finished all the quiz question, now submit it!');
    }
}

/*  back to the user page */
function back_teacher_page(){
    window.open("/user","_self");
}

// for students to go back last page
function back_student_page(){
    window.open("/user","_self");
}

// to load the apge
function loadPage(){
    var target = document.getElementById('url').value;
    console.log(target);
    document.getElementById('iframePosition').src = target;
}

