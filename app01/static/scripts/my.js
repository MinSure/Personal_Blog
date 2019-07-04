function sayhello(){
    alert('say hello')
}

function load_successful(){
    alert('load successful')
}

function checkpwd(){
    var p1=document.forms["form1"].pwd.value;
    var p2=document.forms["form1"].pwd2.value;
    if(p1==""){
        alert("请输入密码！");//检测到密码为空，提醒输入//
    }
    if(p1!=p2){//判断两次输入的值是否一致，不一致则显示错误信息
        alert("两次输入密码不一致，请重新输入");
        }
}
