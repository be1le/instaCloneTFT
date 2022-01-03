function disa() {
    var id = $('#userid').val();
    var password = $('#userpw').val();
    if (id != "" && password !="") {
        $('#login-btn').attr("disabled",false);
        $('#login-btn').css('background-color', 'rgb(75, 186, 255)');
        $("#login-btn").focus()
    }
};



function login() {
    let id = $('#userid').val()
    let password = $('#userpw').val()


    $.ajax({
        type: "POST",
        url: "/api/login",
        data: {id_give: $('#userid').val(), pw_give: $('#userpw').val()},
        success: function (response) {
            if (response['result'] == 'success') {
                // 로그인이 정상적으로 되면, 토큰을 받아옵니다.
                // 이 토큰을 mytoken이라는 키 값으로 쿠키에 저장합니다.
                $.cookie('mytoken', response['token']);
                var login_sound = new Audio();
                login_sound.src = "../static/sounds/Click_Sound_02.mp3"
                login_sound.currentTime = 0;
                login_sound.volume - 1.0;
                login_sound.play();
                // alert('로그인 완료!');
                window.setTimeout(function() {
                    window.location.href = '/main';
                }, 200);

            } else {
                // 로그인이 안되면 에러메시지를 띄웁니다.
                alert(response['msg'])
            }
        }
    })
}


function sign_up() {
    var sign_up_sound = new Audio();
    sign_up_sound.src = "../static/sounds/Signed_up.mp3"
    sign_up_sound.currentTime = 0;
    sign_up_sound.volume - 1.0;
    sign_up_sound.play();
    // alert('로그인 완료!');
    window.setTimeout(function() {
    window.location.href = '/sign';
    }, 400);
}

function getInfo() {
    if ($("#facebook-login").is(":visible")) {
        $("#facebook-login").hide();
    }
    if($("#ready-login").show());
}
    
