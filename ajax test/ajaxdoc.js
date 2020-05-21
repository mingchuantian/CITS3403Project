function get_mark(){
    const table =document.getElementById("table_testing");

    //  Set the url where we create the students
     const url='http://127.0.0.1:5000/students_taken';
    
    //  'Fetching' the information
    fetch(url)
        .then(function(resp){
           return resp.json();
        })
        .then(function(data){
            console.log(data);
            let marks = data.locations;
            console.log(marks);
            
            return marks.map(
                function(mark){
                    let tr = createNode('tr'),
                        td1= createNode('td'),
                        td2= createNode('td');
               
                    td1.innerHTML=mark.name;
                    td2.innerHTML=mark.times;
    
                    append(tr,td1);
                    append(tr,td2);
                    append(table, tr);
                }
            )
            
        })
        
        .catch(function(error){
            console.log(error);
        });
    
        //  Create function to create a node
        function createNode(e){
            return document.createElement(e);
        }
    
        function append(parent,e){
            return parent.appendChild(e);
        }
}


