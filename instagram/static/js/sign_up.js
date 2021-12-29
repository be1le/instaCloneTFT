
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
                alert('회원가입이 완료되었습니다.');
                
                
                
                window.location.href = '/main/good';
                } else {
                    
                    alert(response['msg'])
                }


            } 
        }
    )
}
