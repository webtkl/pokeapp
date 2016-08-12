function type_call(){
    $.ajax({
        method:"GET",
        url:"/typeinfo?type="+$('#call_type').val(),
    }).done( function(response){
             console.log(response)
             console.log("<img source=\""+$(location).attr('href')+ "static/img/" + response.type +".png\">")
             $("#info").html(
                             "<img align=\"middle\" style=\"width: " +$('#info').width() + "px\;  object-fit:contain\" src=\""+$(location).attr('href')+ "static/img/" + response.type +".png\">"

                            )
             $("#weak_against").html(
                                     fillSymbol(response.weak)
                                    )
             $("#vulnerable_to").html(
                                     fillSymbol(response.vul)
                                    )
             $("#strong_against").html(
                                     fillSymbol(response.str)
                                    )
             $("#resistant_to").html(
                                     fillSymbol(response.res)
                                    )

             })
}



function fillSymbol(symbols){
    var symbolArray=symbols.split(',');
    var newHTMLContent="<table align=\"center\" style=\"width:200px\"> <tr>";

    for (var i=0; i < symbolArray.length; i++){
        if ( (i)%4==0 && i!=0){
            newHTMLContent+="</tr><br><tr>"
        }
        newHTMLContent = newHTMLContent + "<td align=\"center\" style=\"min-width:" + $('#resistant_to').width()/4 + "px ; max-width:" + $('#resistant_to').width()/4 +   "\"> <img style=\"width:100%\"  src=\"" + $(location).attr('href')+ "static/img/" + symbolArray[i] +"-sm.png\"> " + "<br>" + "<p style=\"width:100%\">" + symbolArray[i] + "</p></td>"
    }

    newHTMLContent += "</tr></table>"
    return newHTMLContent
}


$("#caller").click(type_call)

