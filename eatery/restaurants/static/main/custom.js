$.getJSON('http://www.geoplugin.net/json.gp?jsoncallback=?', function (data) {
    console.log(JSON.stringify(data, null, 2));
});