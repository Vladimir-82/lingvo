$(document).ready (function () {
    $("#reset").click(function () {
        document.getElementById("text_for_translate").innerHTML = '';
    });
});

function playTrack () {
    var myAudio = document.getElementById("myTune");
    myAudio.play();
    $("#play").hide();
    $("#pause").show();
    }
function pauseTrack () {
    var myAudio = document.getElementById("myTune");
    myAudio.pause();
    $("#play").show();
    $("#pause").hide();
    }
$(document).ready (function () {
    $("#play").bind ("click", playTrack);
    $("#pause").bind ("click", pauseTrack);
});


function playTracktrans () {
    var myTrans = document.getElementById("myTunetrans");
    myTrans.play();
    $("#playtrans").hide();
    $("#pausetrans").show();
    }
function pauseTracktrans () {
    var myTrans = document.getElementById("myTunetrans");
    myTrans.pause();
    $("#playtrans").show();
    $("#pausetrans").hide();
    }
$(document).ready (function () {
    $("#playtrans").bind ("click", playTracktrans);
    $("#pausetrans").bind ("click", pauseTracktrans);
});
