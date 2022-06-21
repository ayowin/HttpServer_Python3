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
            type:"POST",
            url:"http://127.0.0.1:8080/default/verifyCode",
            dataType:"json",
            success:function (data) {
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
            type:"POST",
            url:"http://127.0.0.1:8080/user/login",
            contentType: "application/json", 
            dataType:"json",
            data:requestJson,
            success:function (data) {
                if(data.result == "success"){
                    window.sessionStorage.setItem("token",data.token);
                    location.href = "home.html";
                } else {
                    console.log(data.reason);
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
