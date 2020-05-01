var answer_array=new Array(10000);
for(var answer_total_count=0;answer_total_count<10000;answer_total_count++){
    answer_array[answer_total_count] =new Array();
    for(var jcol=0;jcol<10000;jcol++){
        answer_array[answer_total_count][jcol]="";
    }
}

function check(){
    for(let i=0;i<document.getElementsByName("q1").length;i++){
        if(document.getElementsByName("q1")[i].checked==true){
            //console.log("it is true %d",i)
            document.getElementsByTagName("button")[0].style.backgroundColor="#48C9B0"
            break;
        }else{
            document.getElementsByTagName("button")[0].style.backgroundColor="#F9E79F"
        }
        }

    for(let i=0;i<document.getElementsByName("q2").length;i++){
        if(document.getElementsByName("q2")[i].checked==true){
            //console.log("it is true %d",i)
            document.getElementsByTagName("button")[1].style.backgroundColor="#48C9B0"
            break;
        }else{
            document.getElementsByTagName("button")[1].style.backgroundColor="#F9E79F"
        }
        }

    for(let i=0;i<document.getElementsByName("q3").length;i++){
        if(document.getElementsByName("q3")[i].checked==true){
            //console.log("it is true %d",i)
            document.getElementsByTagName("button")[2].style.backgroundColor="#48C9B0"
            break;
        }else{
            document.getElementsByTagName("button")[2].style.backgroundColor="#F9E79F"
        }
        }
        let count_all=0;
    for(let i=0;i<document.getElementsByName("q4").length;i++){
        
        if(document.getElementsByName("q4")[i].value!=""){
            //console.log("it is true %d",i)
            document.getElementsByTagName("button")[3].style.backgroundColor="#48C9B0"
            count_all++;
            //console.log(count_all);
        }else if(count_all<3){
            document.getElementsByTagName("button")[3].style.backgroundColor="#F9E79F"
            break;
        }
        }

        let count_all_1=0;
    for(let i=0;i<document.getElementsByName("q5").length;i++){
    
        if(document.getElementsByName("q5")[i].value!=""){
            //console.log("it is true %d",i)
            document.getElementsByTagName("button")[4].style.backgroundColor="#48C9B0"
            count_all_1++;
            //console.log(count_all_1);
        }else if(count_all_1<3){
            document.getElementsByTagName("button")[4].style.backgroundColor="#F9E79F"
            break;
        }
        }
    }

    let class_name = "q1";
    var counter_for_question = 0;
    var pointer_array=0;
function save(){
    for(let check_test=0; check_test<document.getElementsByTagName("form")[0].length; check_test++ ){

        if(document.getElementsByTagName("form")[0][check_test].name!=class_name){
            //console.log("they are not same question!");
            class_name = document.getElementsByTagName("form")[0][check_test].name;
            counter_for_question=0;
        }
    if(document.getElementsByTagName("form")[0][check_test].className=="question"){
        //console.log("i am here!");
        if(document.getElementsByTagName("form")[0][check_test].checked==true){
            //console.log(counter_for_question);
                answer_array[0][pointer_array]=counter_for_question;
                pointer_array++;
        }
        }
        counter_for_question++;

        if(document.getElementsByTagName("form")[0][check_test].className=="question_insert"){
            answer_array[0][pointer_array]=document.getElementsByTagName("form")[0][check_test].value
            pointer_array++;
        }
    }
    console.log(answer_array[0]);
    pointer_array=0;
}