$.ajaxSetup({
    data: {
        csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
    }
});

//$('#submit').click(function(){
$('#post-form').submit(function (e) {
    e.preventDefault();
    $('#message').remove();
    var serializedData = $(this).serialize();
    $.ajax({
        url: 'ajax',
        type: 'post',
        data: serializedData,
        async: false,

        success: function (data) {
            //alert(data['msg']+data['pn'])
            /*
            data = JSON.parse(data);
            if (data.status) {
                window.location = data.url
            }
            else {
                alert('fail')
            }
            */
            //alert(data['boardid']);
            if (data.status) {
                $('.boardid').text(data['boardid']);
                document.getElementById('boardid').innerText = data['boardid'];
            } else {
                $('#message').text(data['message']);
            }
            //$('#boardid').innerHTML = data['boardid']  //this is wrong
            /*
            if(data.status) {
                $('.boardid').text(data['boardid'])
            }else{
                $('#message').text(data['message'])
            }*/
        },
        error: function (response) {
            console.log(response)
        }
    })
});