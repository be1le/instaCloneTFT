let elInputUsername = document.querySelector('#username')
//아이디입력
//failure-message hide

let elFailureMessage = document.querySelector(".failure-message")
let elSuccesMessage = document.querySelector(".success-message")


//여기부터 아이디가 유효성을 띄는지 나타내는 함수입니다. 
elInputUsername.onkeyup = function () {
     if(isMoreThan4Length(elInputUsername.value)) {
           //성공메시지가 보여야함
        elSuccesMessage.classList.remove('hide')
           //실패메시지가 가려져야함
        elFailureMessage.classList.add('hide')
  }
   else { 
        //성공메시지가 가려져야함
    elSuccesMessage.classList.add('hide')
       //실패메시지가 보여야함
   elFailureMessage.classList.remove('hide')
  }
}


function isMoreThan4Length(value){
    return value.length >= 4
};
//아이디관련 함수가 끝나는 줄입니다




let elInputPassword = document.querySelector('#password')
//비밀번호입력


let elFailurePassword = document.querySelector('.failure-password')
let elSuccesPassword = document.querySelector(".success-password")


//여기부터 비밀번호가 유효성을 띄는지 나타내는 함수입니다. 
elInputPassword.onkeyup = function () {
     if(isMoreThan8Length(elInputPassword.value)) {
           //성공메시지가 보여야함
        elSuccesPassword.classList.remove('hide')
           //실패메시지가 가려져야함
        elFailurePassword.classList.add('hide')
  }
   else { 
        //성공메시지가 가려져야함
    elSuccesPassword.classList.add('hide')
       //실패메시지가 보여야함
   elFailurePassword.classList.remove('hide')
  }
}


function isMoreThan8Length(value){
    return value.length >= 8
}

////여기부터 비밀번호 재확인 섹션입니다.

let elInputRePassword = document.querySelector('#repassword')
//비밀번호확인 입력


let elFalsePassword = document.querySelector('.false')
let elTruePassword = document.querySelector(".true")


//여기부터 비밀번호가 유효성을 띄는지 나타내는 함수입니다. 
elInputRePassword.onkeyup = function () {
     if(isMoreThan8Length(elInputRePassword.value)) {
           //성공메시지가 보여야함
        elTruePassword.classList.remove('hide')
           //실패메시지가 가려져야함
        elFalsePassword.classList.add('hide')
  }
   else { 
        //성공메시지가 가려져야함
    elTruePassword.classList.add('hide')
       //실패메시지가 보여야함
   elFalsePassword.classList.remove('hide')
  }
}

function isMoreThan8Length(value){
    return value.length >= 8
}
