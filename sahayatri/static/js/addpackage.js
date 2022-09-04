var options = {
    "closeButton": true,
 //   "debug": false,
 //   "newestOnTop": false,
    //"progressBar": true,
   "positionClass": "toast-bottom-right",
 //   "preventDuplicates": false
    "showDuration": "300",
   "hideDuration": "1000",
   "timeOut": "2000",
   "extendedTimeOut": "1000",
   "showEasing": "swing",
   "hideEasing": "linear",
   "showMethod": "fadeIn",
   "hideMethod": "fadeOut"
 }
 $(document).ready(function(){
     $('#packageType').select2();
     $('#catType').select2();
     $('#district').select2(); 
     $('#pname').focus();  
     $('.thumb').hide();  
     $('#thumbnail').hide();  
 
 });   
 imgInp.onchange = evt => {
  if (imgInp.files && imgInp.files.length===4) {
    first.src = URL.createObjectURL(imgInp.files[0])
    second.src = URL.createObjectURL(imgInp.files[1])
    third.src = URL.createObjectURL(imgInp.files[2])
    fourth.src = URL.createObjectURL(imgInp.files[3])
    $('.thumb').show();
  }
  else{
    toastr.error("Invalid Image Numbers!","Please select four images!");
    $('#imgInp').val('');
  }
  
}
thumbImg.onchange = evt => {
  const [thumb]=thumbImg.files;
  debugger;
  if (thumb) {
    thumbnail.src = URL.createObjectURL(thumb)
  }
  $('#thumbnail').show();
}