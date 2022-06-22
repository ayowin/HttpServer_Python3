/**
 * home.js
 */
layui.define(['layer'], function(exports){

    var token = window.sessionStorage.getItem("token");

    if(token == null){
        alert("请您先登录");
        location.href = "index.html";
        return;
    }

    $("#logoutP").click(function(){
        $.ajax({
            headers: {
                token: token
            },
            type:"POST",
            url:"http://127.0.0.1:8080/user/logout",
            dataType:"json",
            success:function (data) {
                if(data.result == "success"){
                    window.sessionStorage.removeItem("token");
                    location.href = "index.html";
                }
            }
        });
    });

    $("#openDoorButton").click(function(){
        $.ajax({
            headers: {
                token: token
            },
            type:"POST",
            url:"http://127.0.0.1:8080/door/open",
            dataType:"json",
            success:function (data) {
                if(data.result == "success"){
                    alert("门已开启！");
                } else {
                    if(data.reason == "unlimited"){
                        alert("没有钥匙！");
                    } else {
                        alert("登录已失效，请重新登录！");
                        window.sessionStorage.removeItem("token");
                        location.href = "index.html";
                    }
                }
            }
        });
    });

    exports('home', {}); 
});

