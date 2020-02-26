var tel=document.getElementById('tel');
var telUyari=document.getElementById('telUyari');
tel.onfocusout=function(){
  telUyari.textContent="";
};
tel.onblur=function(){
  try{
    if(tel.value[0]!=0){throw 'Telefon Numaranız 0 ile başlamalıdır.'}
    if(tel.value[1]!=5){throw 'Lütfen Cep Telefonu Numarınızı Giriniz.'}
    if(tel.value.length!=11){throw 'Telefon Numaranız 11 rakamlı olmalıdır.'}
  }
  catch(e){
    telUyari.textContent=e;
    tel.focus();
  }
}