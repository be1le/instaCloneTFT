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
    // mypage close 사진올리기창에서 새로고침
    $("#close3").click(function(){
      modalClose();  
      window.location.href="/mypage";
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
  // mypage close 글 올리기 창에서 새로고침
  $("#close4").click(function(){
    modalClose();
    window.location.href="/mypage";
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

    let nick = $('#nick').val()
    let file = $(e.target)[0].files[0]
    let form_data = new FormData()

    form_data.append("nick_give", nick)
    if (file) {
        form_data.append("file_give", file)
    }
    $.ajax({
        type: "POST",
        url: "/profile/fileupload",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            alert(response["result"])
            var profile_sound = new Audio();
            profile_sound.src = "../static/sounds/profile.mp3"
            profile_sound.currentTime = 0;
            profile_sound.volume - 1.0;
            profile_sound.play();

            window.setTimeout(function() {
                window.location.href = '/main';
            }, 700);
        }
    });


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
            "height": "300px",
            "border": "0.5px solid lightgray",
            "object-fit": "cover",
            "position": "relative",
            "transform": "translate(50, 50)",
        });
    }else{
      alert('이미지가 아닙니다.');
      return;
    }
}


