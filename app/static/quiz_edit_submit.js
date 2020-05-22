function submit_new_quiz(){
    if(document.getElementsByClassName("quiz").length > 0){
        alert('The quiz creating is not finished already, you can not submit it!');
    }else{
        alert('you finished all the quiz question creating!');
        window.open("/teacher","_self");
    }
}

function submit_quiz_answer(){
    if(document.getElementsByClassName("quiz").length > 0){
        alert('You did not finish all questions, please do not submit it!');
    }else{
        alert('you finished all the quiz question, now submit it!');
        document.getElementsByTagName('button')[2].click();
    }
}

function back_teacher_page(){
    window.open("/teacher","_self");
}

function back_home_page(){
    window.open("/login","_self");
}

function back_student_page(){
    window.open("/student","_self");
}
