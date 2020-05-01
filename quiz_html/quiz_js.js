function check(){
    for(let i=0;i<document.getElementsByName("q1").length;i++){
        if(document.getElementsByName("q1")[i].checked==true){
            console.log("it is true %d",i)
            document.getElementsByTagName("button")[0].style.backgroundColor="#48C9B0"
            break;
        }else{
            document.getElementsByTagName("button")[0].style.backgroundColor="#F9E79F"
        }
        }

    for(let i=0;i<document.getElementsByName("q2").length;i++){
        if(document.getElementsByName("q2")[i].checked==true){
            console.log("it is true %d",i)
            document.getElementsByTagName("button")[1].style.backgroundColor="#48C9B0"
            break;
        }else{
            document.getElementsByTagName("button")[1].style.backgroundColor="#F9E79F"
        }
        }

    for(let i=0;i<document.getElementsByName("q3").length;i++){
        if(document.getElementsByName("q3")[i].checked==true){
            console.log("it is true %d",i)
            document.getElementsByTagName("button")[2].style.backgroundColor="#48C9B0"
            break;
        }else{
            document.getElementsByTagName("button")[2].style.backgroundColor="#F9E79F"
        }
        }
        let count_all=0;
    for(let i=0;i<document.getElementsByName("q4").length;i++){
        
        if(document.getElementsByName("q4")[i].value!=""){
            console.log("it is true %d",i)
            document.getElementsByTagName("button")[3].style.backgroundColor="#48C9B0"
            count_all++;
            console.log(count_all);
        }else if(count_all<3){
            document.getElementsByTagName("button")[3].style.backgroundColor="#F9E79F"
            break;
        }
        }

        let count_all_1=0;
    for(let i=0;i<document.getElementsByName("q5").length;i++){
    
        if(document.getElementsByName("q5")[i].value!=""){
            console.log("it is true %d",i)
            document.getElementsByTagName("button")[4].style.backgroundColor="#48C9B0"
            count_all_1++;
            console.log(count_all_1);
        }else if(count_all_1<3){
            document.getElementsByTagName("button")[4].style.backgroundColor="#F9E79F"
            break;
        }
        }
    }