$(function(s){
  $('.container-ps select').addClass('form-control');
  $('.shmsk select,.shmsk input').addClass('form-control');

  $('.wa').click(function(){
    if ($('.warch').hasClass('dnone')){
      alert("Veillez importer d'abord l'audio dans le champs ci dessous")
    }
  })
  $('.war').click(function(e) {

    $.ajax({
      url:"/dashbord/upload/",
      type:"POST",
      data:$('.demo').serialize(),
      success:function(response) {
        console.log(response);
      },
      error:function(response) {
        console.log('error',response);
      }

    })
  })

})
