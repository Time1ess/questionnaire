$('.save_answer').click(function(){
    save_answer('answer');
});

function save_answer(type)
{
    if(type=='file')
        var callback = callback_file;
    else if(type=='answer')
        var callback = callback_answer;
    else
    {
        alert("保存类型错误!");
        return
    }
    /*var form_data = new FormData($('#answer_sheet')[0]);
    $.ajax({
        type: 'POST',
        url: '/manager/save_answers',
        data: form_data,
        success: callback,
        processData: false,
        cache: false,
        contentType: false,
    });*/
    $("#answer_sheet").ajaxSubmit({
        url: '/manager/save_answers',
        type: 'POST',
        clearForm: false,
        resetForm: false,
        success: callback
    })
}

function callback_file(id_list)
{
    ids = id_list.split(':');
    ids.splice(ids.length-1, 1);
    for(idx in ids)
    {
        div_id = '#status_'+ids[idx];
        $(div_id).removeClass('has-warning').addClass('has-success');
        child_id = div_id + ' div';
        $(child_id).html('覆盖已上传文件:');
        input_id = div_id + ' input';
        $(input_id).val('');
    }
}

function callback_answer(data)
{
    alert(data);
}

$('.file_upload').on('change', function(){
    save_answer('file');
});

$('.confirm_answer').click(function(){
    confirm_answer();
});

function confirm_answer()
{
    var sheet_id = $('#answer_sheet').attr('sheet_id');
    if(!confirm('提交后将无法修改，确认提交？'))
        return;
    $.ajax({
        type: 'POST',
        url: '/manager/confirm_answer',
        data: {'sheet_id':sheet_id},
        success: reload,
    });
}

function reload(data)
{
    if(data=='SUCCESS')
    {
        alert('提交成功！');
        location.reload();
    }
    else
        alert('提交失败，请重新提交');
}

$(':checkbox').on('change', function(){
    var answer = $('#answer_'+$(this).attr('item_id'));
    if($(this).is(':checked'))
        answer.attr('value', 1);
    else
        answer.attr('value', 0);
});
