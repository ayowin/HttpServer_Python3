/**
 * index.js
 */
layui.define(['layer'], function(exports){

    /* 平台自适应 */
    if(navigator.userAgent.indexOf("Mobile") != -1){
        window.location.href = "./indexMobile.html";
        return;
    }

    var verifyCodeId = null;

    var refreshVerifyCode = function(){
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8080/default/verifyCode",
            dataType: "json",
            success: function (data) {
                verifyCodeId = data.id;
                $("#verifyCodeImg").attr("src","data:image/jpeg;base64," + data.base64);
            }
        })
    };

    $("#loginButton").click(function(){
        var requestJson = new Object;
        requestJson.username = $("#usernameInput").val();
        requestJson.password = $("#passwordInput").val();
        requestJson.verify_code_id = verifyCodeId;
        requestJson.verify_code_result = $("#verifyCodeInput").val();
        requestJson = JSON.stringify(requestJson);

        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8080/user/login",
            contentType: "application/json", 
            dataType: "json",
            data: requestJson,
            success: function (data) {
                if(data.result == "success"){
                    window.localStorage.setItem("token",data.token);
                    location.href = "home.html";
                } else {
                    if(data.reason == "invalid verify code"){
                        alert("验证码错误！");
                    } else if(data.reason == "username or password incorrect"){
                        alert("用户名或密码错误！");
                    } else {
                        alert("未知错误，请联系开发者！");
                    }
                }
            }
        });
    });

    $("#registerButton").click(function(){
        var requestJson = new Object;
        requestJson.username = $("#usernameInput").val();
        requestJson.password = $("#passwordInput").val();
        requestJson.verify_code_id = verifyCodeId;
        requestJson.verify_code_result = $("#verifyCodeInput").val();
        requestJson = JSON.stringify(requestJson);

        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8080/user/register",
            contentType: "application/json", 
            dataType: "json",
            data: requestJson,
            success: function (data) {
                if(data.result == "success"){
                    alert("注册成功！");
                    $("#usernameInput").val("");
                    $("#passwordInput").val("");
                    $("#verifyCodeInput").val("");
                } else {
                    if(data.reason == "invalid verify code"){
                        alert("验证码错误！");
                    } else if(data.reason == "insert exception"){
                        alert("用户名已存在！");
                    } else {
                        alert("未知错误，请联系开发者！");
                    }
                }
            }
        });
    });

    $("#verifyCodeImg").click(function(){
        refreshVerifyCode();
    });

    refreshVerifyCode();

    exports('index', {}); 
});
