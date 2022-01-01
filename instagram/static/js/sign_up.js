function is_nickname(asValue) {
    var regExp = /^(?=.*[a-zA-Z])[-a-zA-Z0-9_.]{2,10}$/;
    return regExp.test(asValue);
}

function is_password(asValue) {
    var regExp = /^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,20}$/;
    return regExp.test(asValue);
}



function check_dup() {
    let username = $("#userid").val() 
    
    if (!is_nickname(username)) {
        alert("아이디의 형식을 확인해주세요. 영문과 숫자, 일부 특수문자(._-) 사용 가능. 2-10자 길이")
        $("#userid").focus()
        return;
    }

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
    id= $('#userid').val()
    pw= $('#userpw').val()
    username= $('#username').val()
    nickname= $('#usernick').val()
    check= $('#check').val()

    
    if (id =="") {
        alert('어떻게 왔냐고 돌아가')
        return;
    } else if (check != "확인완료") {
        alert('어떻게 왔어 돌아가')
        return;
    }

    if (pw == "") {
        alert('비밀번호 가져와 돌아가')
        return;
    } else if (!is_password(pw)) {
        alert('너도 비번 가져와 돌아가')
        return;
    } else {
        alert('통과')
    }

    $.ajax({
        type: "POST",
        url: "/sign/register",
        data: {
            id_give : id,
            pw_give : pw,
            name_give : username,
            nickname_give : nickname

            
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


    if (id != "" && password !="" && nick !='' && name !='' && check == '확인완료' ) {
        $('#sign-up-btn').attr("disabled",false);
        $('#sign-up-btn').css('background-color', 'rgb(75, 186, 255)');
        return
    } else {
        $('#sign-up-btn').attr("disabled",true);
        $('#sign-up-btn').css('background-color', 'grey');
        return
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