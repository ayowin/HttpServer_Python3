/**
 * home.js
 */
layui.define(['layer'], function(exports){

    var token = window.localStorage.getItem("token");

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
                    window.localStorage.removeItem("token");
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
            type: "POST",
            url: "http://127.0.0.1:8080/door/open",
            dataType: "json",
            success:function (data) {
                if(data.result == "success"){
                    alert("门已开启！");
                } else {
                    if(data.reason == "token invalid"){
                        alert("登录已失效，请重新登录！");
                        window.localStorage.removeItem("token");
                        location.href = "index.html";
                    } else if(data.reason == "unlimited"){
                        alert("没有钥匙！");
                    } else {
                        alert("未知原因，请联系开发者！");
                    }
                }
            }
        });
    });

    $("#uploadButton").click(function(){
        var formData = new FormData();

        var files = $("#fileInput")[0].files;
        for(i=0;i<files.length;i++){
            formData.append(files[i].name,files[i]);
        }

        $.ajax({
            headers: {
                token: token
            },
            type: "POST",
            url: "http://127.0.0.1:8080/file/upload",
            data: formData,
            /* upload file request need set processData and contentType to false */
            processData: false,
            contentType: false,
            dataType: "json",
            success: function(data) {
                if(data.result == "success"){
                    alert("上传成功！");
                    $("#fileInput").val("");
                } else {
                    if(data.reason == "token invalid"){
                        alert("登录已失效，请重新登录！");
                        window.localStorage.removeItem("token");
                        location.href = "index.html";
                    } else {
                        alert("未知原因，请联系开发者！");
                    }
                }
            }
        })
    });

    exports('home', {}); 
});
