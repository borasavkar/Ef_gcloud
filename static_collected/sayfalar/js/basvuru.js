function showForm1(){
    document.getElementById('form1').style.display="block";
    document.getElementById('form2').style.display="block";
    document.getElementById('form3').style.display="block";
    document.getElementById('krediForm_gonder').style.display="block";
    document.getElementById('emeklidegilimuyari').style.display="none";
    document.getElementById('emekli_misiniz').style.display="none";
    document.getElementById('ad_input').focus();
    
}
function emeklidegilim(){
    document.getElementById('form1').style.display="none";
    document.getElementById('emeklidegilimuyari').style.display="block";
}
