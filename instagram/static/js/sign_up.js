
// 간단한 회원가입 함수입니다.
// 아이디, 비밀번호, 닉네임을 받아 DB에 저장합니다.

// 비밀번호 확인 변수 

var a = true   


function is_nickname(asValue) {
    var regExp = /^(?=.*[a-zA-Z])[-a-zA-Z0-9_.]{2,10}$/;
    return regExp.test(asValue);
}

function is_password(asValue) {
    var regExp = /^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,20}$/;
    return regExp.test(asValue);
}



function check_pw() {
    let pw = $('#userpw').val()
    if (!is_password(pw)) {
        alert("비밀번호의 형식을 확인하세요 영문, 숫자는 1개 씩 무조건 포함, 일부 특수문자 사용 가능, 8-20자 길이")
        a = false
        $('#userpw').focus()
        return;
    } else {
        a = true
        return;
    }
}

function check_dup() {
    let username = $("#userid").val() 
    
    if (!is_nickname(username)) {
        alert("아이디의 형식을 확인해주세요. 영문과 숫자, 일부 특수문자(._-) 사용 가능. 2-10자 길이")
        $("#userid").focus()
        return;
    }
    // $("#help-id").addClass("is-loading")
    $.ajax({
        type: "POST",
        url: "/sign/check_dup",
        data: {
            userid_give: username
        },
        success: function (response) {
            
            if (response["exists"]) {

                alert("이미 존재하는 아이디입니다.")
                $("#userid").focus()
                return;
            } else {
                alert("사용할 수 있는 아이디입니다.")
                $("#check").val('확인완료')
                $("#check").attr('disabled',true)
                $("#userid").attr('disabled',true)
                $("#username").focus()
                return;
            }
            

        }
    });
}




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
            if (response['result']) {

                console.log(response['token']);
                $.cookie ('mytoken', response['token'], {path: '/'});
                
                var login_sound = new Audio();
                login_sound.src = "../static/sounds/Click_Sound_02.mp3"
                login_sound.currentTime = 0;
                login_sound.volume - 1.0;
                login_sound.play();
                // alert('회원가입이 완료되었습니다.');
                window.setTimeout(function() {
                    window.location.href = '/main';
                }, 100);

                } else {
                    
                    alert(response['msg'])
                }


            } 
        }
    )
}



function disa() {
    
    var id = $('#userid').val();
    var password = $('#userpw').val();
    var nick = $('#usernick').val();
    var name = $('#username').val();
    var check = $('#check').val();
    if (id != "" && password !="" && nick !='' && name !='' && check == '확인완료' && true) {
        $('#sign-up-btn').attr("disabled",false);
        $('#sign-up-btn').css('background-color', 'rgb(75, 186, 255)');
    }
};


function back_to_login() {

    var profile_sound = new Audio();
    profile_sound.src = "../static/sounds/Click_Sound_03.mp3"
    profile_sound.currentTime = 0;
    profile_sound.volume - 1.0;
    profile_sound.play();
    
    window.setTimeout(function() {
    window.location.href = '/';
    }, 300);
    
}