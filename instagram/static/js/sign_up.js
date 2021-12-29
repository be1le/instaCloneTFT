
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
                alert('회원가입이 완료되었습니다.')
                if (response['result'] == 'success') {
                    // 로그인이 정상적으로 되면, 토큰을 받아옵니다.
                    // 이 토큰을 mytoken이라는 키 값으로 쿠키에 저장합니다.
                    $.cookie('mytoken', response['token']);
    
                    window.location.href = '/main'
                } else {
                    
                    alert(response['msg'])
                }

            } else {
                alert(response['msg'])
            }
        }
    })
}
