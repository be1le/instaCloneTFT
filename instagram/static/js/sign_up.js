
// 간단한 회원가입 함수입니다.
// 아이디, 비밀번호, 닉네임을 받아 DB에 저장합니다.
function register() {
    $.ajax({
        type: "POST",
        url: "/sign/register",
        data: {
            id_give: $('#userid').val(),
            pw_give: $('#userpw').val(),
            name_give : $('#username').val(),
            nickname_give: $('#usernick').val()
            
        },
        success: function (response) {
            if (response['result'] == 'success') {

                console.log(response['token']);
                $.cookie ('mytoken', response['token'], {path: '/'});
                
                var login_sound = new Audio();
                login_sound.src = "../static/sounds/Click_Sound_02.mp3"
                login_sound.currentTime = 0;
                login_sound.volume - 1.0;
                login_sound.play();
                // alert('회원가입이 완료되었습니다.');
                window.setTimeout(function() {
                    window.location.href = '/main/good';
                }, 100);

                } else {
                    
                    alert(response['msg'])
                }


            } 
        }
    )
}
