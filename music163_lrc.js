(function () {
    var timeout = 1000;
    if (document.querySelector("div.listbd") == null) {
        document.querySelector("a[title=播放列表]").click();
        timeout = 5000;
    }
    setTimeout(function () {
        var lrc_list = Array.prototype.slice.call(document.querySelectorAll("#g_playlist .listlyric>p"));
        var lrc_text = "";
        for (var key in lrc_list) {
            var time = parseFloat(lrc_list[key].getAttribute('data-time'));
            var minute = ('0' + parseInt(time / 60)).substr(-2);
            var second = ('0' + (time % 60).toFixed(3)).substr(-6);
            lrc_text += '[' + minute + ':' + second + '] ' + lrc_list[key].innerHTML.replace('<br>', '  ') + '\n';
        }
        var link = document.createElement("a");
        link.href = 'data:text/plain;charset=utf-8,' + encodeURIComponent(lrc_text);
        link.setAttribute("download", player.getPlaying().track.name + '.lrc');
        link.click();
    }, timeout);
})();