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
  $('#district').select2(); 
  $('#pname').focus();  
  $('.thumb').hide();  
  $('#thumbnail').hide(); 
  localStorage.setItem('inclusions',
  `Tour Cost Includes:
  1. Accommodation as per plan.
  
  2. All inter transfer & sightseeing as per Itinerary by Suitable NON AC Vehicle.
  
  PLS. NOTE THAT VEHICLE WILL NOT BE ON DISPOSAL. IT WILL BE PROVIDED AS PER ITINERARY AND POINT TO POINT BASIS
  
   3. News paper and bottled water on arrival.
  
  4. All parking and permit charges.
  
  5. Assistance on arrival.`)
  localStorage.setItem('exclusions',`The Cost Doesn’t Include:
  1. Government Service Tax as applicable on the above rates
  
  2. Airfare, Train Fare, Insurance Premium etc.
  
  3. Entry Fee to Any Monument, Park, Museum, Monastery or any other visiting places.
  
  4. Payment for service provided on personal basis
  
  5. Expenses incurred due to mishap, landslide, strikes, political unrest etc. In such cases extra will    be charged as per actual
  
  6. Cost for services which is not mentioned in “Inclusions”
  
  7. Personal expenses on items such as Laundry, Soft & Hard Drinks, Bottle Water, Incidentals,   Porterage, and Bell-Boy charges, Tips etc.`)
  localStorage.setItem('itnerary',`Day 1: Join Kathmandu, reception from airport and transfer to hotel in Thamel
  Day 2: Kathmandu – city of temples visit Pashupatinath, Boudhanath Stupa, Monkey Temple, and Patan.
  Day 3: Drive to Namobuddha and hike to Balthali village resort.
  Day 4: Drive to Bhaktapur and sightseeing and transfer to hotel 
  Day 5: Transfer to airport, farewell. `)

     $('#packageType').select2();
     $('#province').select2();
     $('#muni').select2();     
     $('#overview').summernote();     
     $('#inclusion').summernote();     
     $('#exclusion').summernote();     
     $('#itnerary').summernote(); 
     $('#datetime').datepicker({
      format: "yyyy-mm-dd",
     });    
     $('#pname').keydown(function(e){
      if(e.keyCode==13){
          if( $('#pname').val()==""|| $('#pname').val()==null){
          toastr.error("Cannot leave null field","Error");
          $('#pname').focus();
          return false;        
          }
          else{
            e.preventDefault();
            $('#price').focus();
          }      
      }  
    });
    $('#price').keydown(function(e){
      if(e.keyCode==13){
          if( $('#price').val()==0|| $('#price').val()==null){
          toastr.error("Cannot leave null field","Error");
          $('#price').focus();
          return false;        
          }
          else{
            e.preventDefault();
            $('#desc').focus();
          }      
      }  
    });
    
    $('#desc').keydown(function(e){
      if(e.keyCode==13){
          if( $('#desc').val()==""|| $('#desc').val()==null){
          toastr.error("Cannot leave null field","Error");
          $('#desc').focus();
          return false;        
          }
          else{
            e.preventDefault();
            $('#nights').focus();
          }      
      }  
    });
    $('#nights').keydown(function(e){
      if(e.keyCode==13){
          if( $('#nights').val()==0|| $('#nights').val()==null){
          toastr.error("Cannot leave null field","Error");
          $('#nights').focus();
          return false;        
          }
          else{
            e.preventDefault();
            $('#days').focus();
          }      
      }  
    }); 
    $('#days').keydown(function(e){
      if(e.keyCode==13){
          if( $('#days').val()==0|| $('#days').val()==null){
          toastr.error("Cannot leave null field","Error");
          $('#days').focus();
          return false;        
          }
          else{
            e.preventDefault();
            $('#packageType').focus();
          }      
      }  
    }); 
 
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
  if (thumb) {
    thumbnail.src = URL.createObjectURL(thumb)
  }
  $('#thumbnail').show();
}
$('#packageType').on('select2:select', function (e) {
  var ptype = $('#packageType').val();
  if(ptype==0 || ptype==null ){
    toastr.error("Error!","Please Select Package Type!");    
  }
  else{
    e.preventDefault();
    $('#catType').focus();     
  }  
});
$('#catType').on('select2:select', function (e) {
  var ctype = $('#catType').val();
  if(ctype==0 || ctype==null ){
    toastr.error("Error!","Please Select Package Type!");    
  }
  else{
    e.preventDefault();    
     $('#district').focus();    
  }  
});

$('#province').on('select2:close', function () {
  var prov=$('#province').val();
  url=$('#url').data('url'); 
  var csrftoken = $("[name=csrfmiddlewaretoken]").val();
  $.ajax({
    url:url,
    type:"POST",
    dataType:"json",
    data:{pid:prov},
    headers: {
      "X-CSRFToken": csrftoken
    },
    success:function(data){
      var html="";
      var list=data.dist;
      for(i=0;i<list.length;i++){
        html+="<option value="+list[i].id+">"+ list[i].name+"</option>"        
      }       
        $('#district').html(html);
        $('#district').focus();
    },
    error:function(){
      toastr.error("Error!","District not found!");
    }
  });
});

$('#district').on('select2:close', function () {
  var mid=$('#district').val();
  url=$('#url1').data('url'); 
  var csrftoken = $("[name=csrfmiddlewaretoken]").val();
  $.ajax({
    url:url,
    type:"POST",
    dataType:"json",
    data:{mid:mid},
    headers: {
      "X-CSRFToken": csrftoken
    },
    success:function(data){
      var html="";
      var list=data.muni;
      for(i=0;i<list.length;i++){
        html+="<option value="+list[i].id+">"+ list[i].name+"</option>"       
      }       
        $('#muni').html(html);
        $('#muni').focus();
    },
    error:function(){
      toastr.error("Error!","Municipality not found!");
    }
  });
});

$('#overview').keydown(function(e){
  if(e.keyCode==13){
      if( $('#overview').val()==""|| $('#overview').val()==null){
      toastr.error("Cannot leave null field","Error");
      $('#overview').focus();
      return false;        
      }
      else{
        e.preventDefault();
        $('#thumbImg').focus();
      }      
  }  
}); 
function InsertPackage(act){
  var url=$('#url2').data('url');
  var csrftoken = $("[name=csrfmiddlewaretoken]").val();
  debugger;
  if( $('#pname').val()==""|| $('#pname').val()==null){
    toastr.error("Cannot leave null package name field","Error");
  }
  else if($('#price').val()==0|| $('#price').val()==null){
    toastr.error("Cannot leave null price field","Error");
  }
  else if($('#desc').val()==0|| $('#desc').val()==null){
    toastr.error("Cannot leave null description field","Error");
  }
  else if($('#nights').val()==0|| $('#nights').val()==null){
    toastr.error("Cannot leave null duration field","Error");
  }
  else if($('#days').val()==0|| $('#days').val()==null){
    toastr.error("Cannot leave null duration field","Error");
  }
  else if($('#overview').summernote('code')==0|| $('#overview').summernote('code')==null){
    toastr.error("Cannot leave null overview field","Error");
  }
  else if($('#packageType').val()==0|| $('#packageType').val()==null){
    toastr.error("Cannot leave null package type field","Error");
  }
  else if($('#province').val()==0|| $('#province').val()==null){
    toastr.error("Cannot leave null provice field","Error");
  }else if($('#muni').val()==0|| $('#muni').val()==null){
    toastr.error("Cannot leave null municipality field","Error");
  }
  else if($('#district').val()==0|| $('#district').val()==null){
    toastr.error("Cannot leave null district field","Error");
  }
  else if($('#catType').val()==0|| $('#catType').val()==null){
    toastr.error("Cannot leave null category field","Error");
  }else{    
      var action=act;      
      var pname=$('#pname').val();
      var price=$('#price').val();
      var desc=$('#desc').val();
      var nights=$('#nights').val();
      var days=$('#days').val();
      var overview=$('#overview').summernote('code');
      var packageType=$('#packageType').val();
      var province=$('#province').val();
      var district=$('#district').val();
      var muni=$('#muni').val();
      var catType=$('#catType').val();
      var inclusions=$('#inclusion').summernote('code');
      var exclusions=$('#exclusion').summernote('code');
      var itner=$('#itnerary').summernote('code');
      var location='N/A'//$('#mapURL').val()'';
      var discount='0'//$('#discount').val();
      var vdate=$('#datetime').val();   
      //FormData initialized
      var data=new FormData();
      data.append("action",action);
      data.append("img1",$("input[id^='imgInp']")[0].files[0]);      
      data.append("img2",$("input[id^='imgInp']")[0].files[1]);      
      data.append("img3",$("input[id^='imgInp']")[0].files[2]);      
      data.append("img4",$("input[id^='imgInp']")[0].files[3]);      
      data.append("thumbImg",$("input[id^='thumbImg']")[0].files[0]);
      data.append("pname",pname);
      data.append("price",price);
      data.append("desc",desc);
      data.append("nights",nights);
      data.append("days",days);
      data.append("overview",overview);
      data.append("packageType",packageType);
      data.append("province",province);
      data.append("district",district); 
      data.append("muni",muni);
      data.append("catType",catType);
      data.append("inclusions",inclusions);
      data.append("exclusions",exclusions);
      data.append("itner",itner);
      data.append("location",location);
      data.append("discount",discount);
      data.append("vdate",vdate);
         
    $.ajax({
      url:url,
      type:"POST",
      dataType:"json",
      processData:false,
      contentType:false,
      mimeType:"multipart/form-data",
      data:data,
      headers: {
        "X-CSRFToken": csrftoken
      },
      success:function(data){
          toastr.success('Successfully Added Package!');
          
      },
      error:function(){
          toastr.error("Unable to insert","Error",options);
      }
  });
  }
  
}


$('#checkin').on('click',function(){
  if($(this).prop('checked')==true){
    $('#inclusion').summernote('code',localStorage.getItem('inclusions'));
  }
  else{
    $('#inclusion').summernote('code','');
  }
});

$('#checkex').on('click',function(){
  if($(this).prop('checked')==true){
    $('#exclusion').summernote('code',localStorage.getItem('exclusions'));
  }
  else{
    $('#exclusion').summernote('code','');
  }
});
$('#checkit').on('click',function(){
  if($(this).prop('checked')==true){
    $('#itnerary').summernote('code',localStorage.getItem('itnerary'));
  }
  else{
    $('#itnerary').summernote('code','');
  }
});
