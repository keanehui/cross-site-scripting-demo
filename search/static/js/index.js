function setSafeInput() {
    $("#input_box").val("Hello World");
}

function setUnsafeInput() {
    $("#input_box").val("Hello<script src='../static/js/malicious.js'></script> World");
}

function clearInput() {
    $("#input_box").val("");
}

$(document).ready(function() {
    $("#auto_fill_button_1").on("click", setSafeInput);
    $("#auto_fill_button_2").on("click", setUnsafeInput);
    $("#clear_button").on("click", clearInput);
});