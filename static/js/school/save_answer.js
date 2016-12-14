function save(type) {
    if (type == 'answer') save_callback=answer_callback;
    else if (type == 'file') save_callback=file_callback;
    else return;

    //form_data = new FormData($("#school_sheet")[0]);
    /*form_data = $("#school_sheet").serialize();
    
    $.ajax({
        type: 'POST',
        data: form_data,
        url: '/school/answer_save',
        success: save_callback,
        processData: false,
        cache: false,
        contentType: false
    });*/
    $("#school_sheet").ajaxSubmit({
        url: '/school/answer_save',
        type: 'POST',
        clearForm: false,
        resetForm: false,
        success: save_callback
    })
}

$(".save_answer").click(function(){
    save('answer');
});

function answer_callback(id_list) {
    /*ids = id_list.split(",")
    for (id in ids) {

    }*/
   alert("保存成功");
}


$(".file_upload").on('change', function(){
    save('file')
});

function file_callback(data) {
    //j_data = JSON.parse(data);
    //ids = j_data.file;
    ids = data.split(',');
    for (idx in ids) {
        id = ids[idx]
        file_div = "#status_" + id;
        $(file_div).removeClass("has-warning").addClass("has-success");
        child_div = file_div + " div";
        $(child_div).html('覆盖已上传文件');
        input = file_div + " input";
        $(input).val('');
    }
}

$(':checkbox').on('change', function() {
    var answer = $('#answer_'+$(this).attr('item_id'));
    if($(this).is(':checked'))
        answer.attr('value', 1);
    else
        answer.attr('value', 0);
});

$('.confirm_answer').click(function() {
    confirm_answer();
});

function confirm_answer() {
    var sheet_id = $('#school_sheet').attr('sheet_id');
    if(!confirm('提交后将无法修改，确认提交？'))
        return;
    $.ajax({
        type: 'POST',
        url: '/school/answer_confirm',
        data: {'sheet_id':sheet_id},
        success: reload
    });
}

function reload(data) {
    if(data=='SUCCESS')
    {
        alert('提交成功！');
        location.reload();
    }
    else
        alert('提交失败，请重新提交');
}
