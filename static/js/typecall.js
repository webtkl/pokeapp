function type_call(){
    $.ajax({
        method:"GET",
        url:"/typeinfo?type="+$('#call_type').val(),
    }).done( function(response){
             console.log(response)
             console.log("<img source=\""+$(location).attr('href')+ "static/img/" + response.type +".png\">")
             $("#info").html(
                             "<img source=\""+$(location).attr('href')+ "static/img/" + response.type +".png\">"
                            )
             })
}

$("#caller").click(type_call)