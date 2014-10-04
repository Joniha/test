function logic(model, tables, update, test){

    $("label").remove();
        $("input:button").remove();
        var header = tables[1];
        var type = tables[0];
        var _id;
        var _st;
        var select = '';
        var select0 = '';
        $("#table_obj").html('');
        $("#table_obj").append('<tr id="head"></tr>');
        $.each(tables, function(key, val){
            if (key !=0){
                $("#table_obj").append('<tr id="str'+ key +'"><tr>');
                    if (key == 1){
                    $.each(val, function(id, value){$("#head").append('<th>'+value+'</th>');});
                    }
                else{
                    $.each(val,function(id, value){
                    $("#str"+key).append('<th id="p'+key+id+'"></th>');
                    $("#p"+key+id).append('<label id="l'+ id + key +'">'+ value +'</label>');
                    });
                    }
                }
            });

        $.each(tables, function(key, val){
                $.each(val,function(id, value){
                    $("#p"+key+id).bind('dblclick', function(eventObject){
                    $("#send1").remove();
                    $("<input type='button' id='send1' value='change'/>").appendTo("#table_obj");
                             var temp_id = id;
                             $("#update").replaceWith('<label id="'+ select0 +'">'+ select +'</label>');
                                if (type[temp_id-1] == "char"){
                                    $("#l"+ id +key).replaceWith('<input type="text" name="_" id="update" required>');
                                    }
                                else if (type[temp_id-1] == "int"){
                                    $('<input type="number" name="_"  id="update" number required>').replaceAll("#l"+ id + key);
                                     }
                                else if (type[temp_id-1] == "date"){
                                     $('<input type="date" name="_" id="update" required>').replaceAll("#l"+ id +key);
                                     $( "#update" ).datepicker({ dateFormat: "yy-mm-dd" });
                                     }
                            select = value;
                            select0 = "l"+ id + key;
                            _id = id;
                            _st = key-1;
                            });
                    });
        $('#send1').live('click', function(eventObject){
                var res = "_" + model + "_" + _st + "_" + _id +"_" +$('#update').val();
                        if (res != ' '){
                                        ajax(res, update);
                                        }
                        });
                });

        var i =0;
        $.each(header, function(key, name){
            if (key !=0){
                if (type[i] == "char"){
                    $('<label id="v">'+name+'<input type="text" name="_" id="insert" required></label>').appendTo("#add");
                    }
                if (type[i] == "int"){
                    $('<label id="v">'+name+'<input type="number" name="_" id="insert" number required></label>').appendTo("#add");
                    }
                if (type[i] == "date"){
                     $('<label id="v">'+name+'<input type="date" name="_" id="dat" required></label>').appendTo("#add");
                     $( "#dat" ).datepicker({ dateFormat: "yy-mm-dd" });
                     }
                i+=1;
                }
            });

        $("<input type='button' id='send0' value='Ok'/>").appendTo("#but");
        $('#send0').bind('click', function(eventObject){
            var input = model;
            $("input").each(function(i){
                        if ($(this).val() !="Ok"){input +=  "_" + $(this).val();}
                        });
                        if (input){
                               ajax(input, test);
                                  }
                        });

}
function ajax(param, _url){
            $.ajax({
               type: "GET",
               url: _url,
               data: {'my':param},
               dataType: "json",
               success:function(){
                    location.reload();
                    },
               error:function(){
                    //alert("Error");
                    }
               });

            }
