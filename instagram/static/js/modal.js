$(function post(){
    $("#confirm").click(function(){
        modalClose();
        //컨펌 이벤트 처리
    });
    $("#modal-open").click(function(){$("#popup").css('display','flex').hide().fadeIn();
    });
    $("#close").click(function(){
        modalClose();  
        window.location.href="/main";
    });

    function modalClose(){
      $("#popup").fadeOut();
    }
  });

  $(function(){
    $("#confirm").click(function(){$("#popup2").css('display','flex').hide().fadeIn();
  });
    $("#confirm2").click(function(){
        modalClose();
        //컨펌 이벤트 처리
    });
    $("#close2").click(function(){
      modalClose();
      window.location.href="/main";
  });
    function modalClose(){
      $("#popup2").fadeOut();
    }
  });

  function resize(obj) {
    obj.style.height = "0.5px";
    obj.style.height = (12+obj.scrollHeight)+"px";
  }

  $('div.popup.popup-body')
  .on("dragover", dragOver)
  .on("dragleave", dragOver)
  .on("drop", uploadFiles);

function dragOver(e){
  e.stopPropagation();
  e.preventDefault();
  if (e.type == "dragover") {
    $('.modalimg').css('display', 'block');
    $('.body-content').remove();
    
  } 
    
}

function uploadFiles(e) {
    e.stopPropagation();
    e.preventDefault();
    dragOver(e);
  
    e.dataTransfer = e.originalEvent.dataTransfer;
    var files = e.target.files || e.dataTransfer.files;
    if (files.length > 1) {
        alert('하나만 올려라.');
        return;
    }
    if (files[0].type.match(/image.*/)) {
                $(e.target).css({
            "background-image": "url(" + window.URL.createObjectURL(files[0]) + ")",
            "outline": "none",
            "background-size": "100% 100%",
            "width": "300px",
            "height": "300px"
        });
    }else{
      alert('이미지가 아닙니다.');
      return;
    }
}

