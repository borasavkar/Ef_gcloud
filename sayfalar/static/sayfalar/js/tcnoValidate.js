var nesne=document.getElementById("tc_input");
var uyari=document.getElementById("tc_uyari");
nesne.onblur=function(){
	uyari.textContent="";
};
nesne.onblur=function(){
	try{
		if(nesne.value.length==0){throw "Lütfen T.C. Kimlik Numarınızı Girin."}
		else if(nesne.value[0]==0){throw "T.C. Kimlik No 0 ile başlayamaz."}
		else if(nesne.value.length<11 && nesne.value>1){throw "11 karakterden az girdiniz."}
		else if(nesne.value.length>11){throw "11 karakterden fazla girdiniz."}
		else if(nesne.value[9] != (((Number(nesne.value[0])+Number(nesne.value[2])+Number(nesne.value[4])+Number(nesne.value[6])+Number(nesne.value[8]))*7)-(Number(nesne.value[1])+Number(nesne.value[3])+Number(nesne.value[5])+Number(nesne.value[7])))%10){throw "TC Kimlik Numaranızın 10. hanesini yanlış girdiniz."}
		else if(nesne.value[10] != (Number(nesne.value[0])+Number(nesne.value[1])+Number(nesne.value[2])+Number(nesne.value[3])+Number(nesne.value[4])+Number(nesne.value[5])+Number(nesne.value[6])+Number(nesne.value[7])+Number(nesne.value[8])+Number(nesne.value[9]))%10){ throw "TC Kimlik Numaranızın son hanesini yanlış girdiniz."}
	}
	catch(e){	
	uyari.textContent=e;
	nesne.focus();
	}
};