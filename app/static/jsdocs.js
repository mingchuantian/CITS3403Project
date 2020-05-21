function loadPage(){
    var target = document.getElementById('url').value;
    console.log(target);
    document.getElementById('iframePosition').src = target;
}
