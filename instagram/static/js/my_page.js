/*
*******************************************************************************************************************
날일 : 초안일 (2021-12-22 水曜日)  |   수정일     : 2021-12-24 今曜日 수정자 : 조시욱
저자 : 조시욱                     |  진행 저자   : 수정 하시면 수정자랑 진행저자에 성함 적으시면됩니다.
제목 : simple js
내용 : 실무에 가장 유용하게 쓰이는 시간 단축 매크로 파일입니다.
버전 : 21.12.24
*******************************************************************************************************************
*/

// console.log 테스트 라인 ++ HOW-TO-USE : Ctrl + / 로 주석 해제 후 console.log('입력문구'); ++
// *******************************************************************************************************************
// console.log('안녕하세요 성기훈 입니다.');
// const console_log_out = prompt('입력할 값을 넣으세요 :');
// *******************************************************************************************************************

//#region simple js [1] 자주 쓰이는 매크로 라인
// *******************************************************************************************************************
// 1) alert(알림) 매크로
// ex) Test_Alert('Test_Text')
function alert_Value(Test_Text) {
    if (Test_Text == null) {
        return alert('입력 텍스트가 누락되었습니다')
    }
    return alert(Test_Text)
}

// 2) insert(주입) 매크로
// ex) insert_Value('Address','insertvalue')
function insert_Value(Address, insertvalue) {
    const Show_Insert_Val = $(Address).val(insertvalue)
    if (Address == null || insertvalue == null) {
        return alert('주소값 또는 밸류값이 누락되었습니다.')
    }
    return Show_Insert_Val;
}

// 3) append(추가) 매크로
// ex) Append_Value('Address','add_child')
function append_Value(Address, add_child) {
    const Show_Append_Val = $(Address).append(add_child)
    if (Address == null || add_child == null) {
        return alert('주소값 또는 추가되어질 오브젝트가 누락되었습니다.')
    }
    return Show_Append_Val;
}

//#region  오브젝트 find by query 매크로

const query_to_address = {
// 1) Query_Value(싱글쿼리 찾기) 매크로
// ex) Query_Value('# or.Query_to_Address li ul ol ...')
    Query_Value: function (Query_to_Address) {
        const Show_Query_Val = document.querySelector(Query_to_Address)
        if (Query_to_Address == null) {
            return alert('쿼리 주소값이 누락되었습니다.')
        }
        return Show_Query_Val;
    },
// 2) QueryAll_Value(모든쿼리 찾기) 매크로
// ex) QueryAll_Value('# or.QueryAll_to_Address li ul ol ...')
    QueryAll_Value: function (QueryAll_to_Address) {
        const Show_QueryAll_Val = document.querySelectorAll(QueryAll_to_Address)
        if (QueryAll_to_Address == null) {
            return alert('쿼리 주소값이 누락되었습니다.')
        }
        return Show_QueryAll_Val;
    }
}

//#endregion

//#region  오브젝트 change by query 매크로

const change_address_text = {
// 1) change_text_byQuery(싱글쿼리 텍스트 바꾸기) 매크로
// ex) change_text_byQuery('Query_to_Address', 'change_Text')
    change_text_byQuery: function (Query_to_Address, change_Text) {
        const change_text_Query_Val = document.querySelector(Query_to_Address)
        if (Query_to_Address == null) {
            return alert('텍스트를 바꿀 쿼리 주소값이 누락되었습니다.')
        }
        return change_text_Query_Val.innerText = change_Text;
    },
// 2) change_text_byQueryAll(모든쿼리 텍스트 바꾸기) 매크로
// ex) change_text_byQueryAll('QueryAll_to_Address', 'change_Text')
    change_text_byQueryAll: function (QueryAll_to_Address, change_Text) {
        const change_text_QueryAll_Val = document.querySelectorAll(QueryAll_to_Address)
        if (QueryAll_to_Address == null) {
            return alert('텍스트를 바꿀 쿼리 주소값이 누락되었습니다.')
        }
        return change_text_QueryAll_Val.innerText = change_Text;
    }
}

//#endregion

//#region  오브젝트 show and hide 매크로

const show_and_hide = {
// 4) show(보여주기) 매크로
// ex) show_Value('Address')
    show_Value: function (Address) {
        const Show_Val = $(Address).show()
        if (Address == null) {
            return alert('보여질 주소가 누락되었습니다')
        }
        return Show_Val;
    },
// 5) hide(숨기기) 매크로
// ex) hide_Value('Address')
    hide_Value: function (Address) {
        const Show_Hide_Val = $(Address).hide()
        if (Address == null) {
            return alert('숨길 주소가 누락되었습니다')
        }
        return Show_Hide_Val;
    }
}

//#endregion

//#region  리스트 push,clear 매크로

// 6) push(리스트에 아이템 추가) 매크로
// ex) push_Value('location','item')
function push_Value(location, item) {
    try {
        const push_Val = location.push(item)
        if (item == null) {
            alert_Value('아이템 값이 누락되었습니다')
        } else {
            return push_Val;
        }
    } catch {
        alert_Value('아무런 값도 입력되지 않았습니다.')
    }
}

//#endregion

// *******************************************************************************************************************
//#endregion

//#region simple js [2] 사칙연산 매크로 라인

// *******************************************************************************************************************
const calulator = {
// 1) Summary(더하기) 매크로
// ex) Summary_Value(Param1,Param2, ..., ...)
    Summary_Value: function (...Param) {
        let sum_Result = 0;
        if (Param.length <= 1) {
            return alert('덧셈식은 두개의 값 이상이여야합니다.')
        }
        for (let i = 0; i < Param.length; i++) {
            sum_Result += Param[i]
        }
        return sum_Result;
    },
// 2) Multiply(곱하기) 매크로
// ex) Multiply_Value(Param1,Param2, ..., ...)
    Multiply_Value: function (...Param) {
        let Multiply_Result = 1;
        if (Param.length <= 1) {
            return alert('곱셈식은 두개의 값 이상이여야합니다.')
        }
        for (let i = 0; i < Param.length; i++) {
            Multiply_Result *= Param[i]
        }
        return Multiply_Result;
    },
// 3) Sqaured(거듭제곱) 매크로
// ex) squared_Value(Param1,Param2)
    squared_Value: function (Param1, Param2) {
        if (Param1 == 1) {
            return alert('거듭 제곱은 2부터 가능합니다.')
        } else if (Param2 == null || Param1 == null) {
            return alert('밑 또는 지수가 누락되었습니다.')
        } else if (Param1 * Param2 == 0) {
            return Param1;
        } else {
            return Param1 ** Param2;
        }
    }
}



// *******************************************************************************************************************
//#endregion

//#region simple js [3] 이벤트 리스너
// *******************************************************************************************************************
// function handleObjectClick(){event} 변경사항.
// Object.addEventListener('click',handleObjectClick); 마우스 클릭 이벤트
// Object.onclick = handleOjbectClick; 클릭 마우스 이벤트  클릭!
// function handleMouseEnter(){event} 변경사항.
// Object.addEventListener('mouseenter',handleMouseEnter); 마우스 엔터 이벤트
// function handleMouseLeave(){event} 변경사항.
// Object.addEventListener('mouseleave',handleMouseLeave); 마우스 리브 이벤트
// Object.removeEventListener(handleObjectClick) 이런식으로 이벤트 리스너 삭제 가능함.
// *******************************************************************************************************************
//#endregion


// 로그아웃  


function logout(){
    $.removeCookie('mytoken', {path: '/'});
    // alert('로그아웃!')
    
    
    var logout_sound = new Audio();
    logout_sound.src = "../static/sounds/Page_Turned.mp3"
    logout_sound.currentTime = 0;
    logout_sound.volume - 1.0;
    logout_sound.play();
    
    window.setTimeout(function() {
        window.location.href='/';
    }, 400);
}

function mypage(){

    var mypage_sound = new Audio();
    mypage_sound.src = "../static/sounds/Click_Sound_03.mp3"
    mypage_sound.currentTime = 0;
    mypage_sound.volume - 1.0;
    mypage_sound.play();
    
    window.setTimeout(function() {
        window.location.href='/mypage';
    }, 200);
}

function home(){
    var home_sound = new Audio();
    home_sound.src = "../static/sounds/Page_Turned.mp3"
    home_sound.currentTime = 0;
    home_sound.volume - 1.0;
    home_sound.play();
    
    window.setTimeout(function() {
        window.location.href = '/main';
    }, 300);
}

function like(){
    
    
    document.getElementById("like").src = "../static/images/instagram_like.png";
    var home_sound = new Audio();
    home_sound.src = "../static/sounds/Page_Turned.mp3"
    home_sound.currentTime = 0;
    home_sound.volume - 1.0;
    home_sound.play();
    
}

function save() {
    document.getElementById("save").src = "../static/images/save_color.png";
    var home_sound = new Audio();
    home_sound.src = "../static/sounds/Page_Turned.mp3"
    home_sound.currentTime = 0;
    home_sound.volume - 1.0;
    home_sound.play();
    
}

<<<<<<< Updated upstream
function profile(){
    
    var profile_sound = new Audio();
    profile_sound.src = "../static/sounds/profile.mp3"
    profile_sound.currentTime = 0;
    profile_sound.volume - 1.0;
    profile_sound.play();

    window.setTimeout(function() {
        window.location.href = '/profile';
    }, 700);
    
}

function change_pw() {
    var profile_sound = new Audio();
    profile_sound.src = "../static/sounds/profile.mp3"
    profile_sound.currentTime = 0;
    profile_sound.volume - 1.0;
    profile_sound.play();

    window.setTimeout(function() {
        window.location.href = '/change_pw';
    }, 700);
}
=======
// 게시물 저장됨 이미지 upper-line
let horizontalBar = document.getElementById("horizontal-underline");
let horizontalMenus = document.querySelectorAll("nav:first-child a");

function horizontalIndicator(e) {
  horizontalBar.style.left = e.offsetLeft + "px";
  horizontalBar.style.width = e.offsetWidth + "px";
  horizontalBar.style.top = e.offsetTop + e.offsetHeight + "px";
}

horizontalMenus.forEach((menu) =>
  menu.addEventListener("click", (e) =>
    horizontalIndicator(e.currentTarget)
  )
);
>>>>>>> Stashed changes
