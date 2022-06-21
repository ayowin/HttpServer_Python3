/**
 * indexMobile.js
 */
 layui.define(['layer'], function(exports){

    /* 平台自适应 */
    if(navigator.userAgent.indexOf("Mobile") == -1){
        window.location.href = "./index.html";
        return;
    }

 });