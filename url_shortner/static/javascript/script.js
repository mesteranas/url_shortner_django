alert("hi")
function Copy(){
    e=document.getElementById("result")
    e.select()
    document.execCommand("copy")
    e.focace()
}
function openURL(){
    e=document.getElementById("copy").value
    window.location.href=e
}