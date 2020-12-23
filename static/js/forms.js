
$(document).ready(function() {
    $('#add_more').click(function() {
       
        var form_idx = $('#id_form-TOTAL_FORMS').val();
        $('#form_set').append($('#id_empty_form').html().replace(/__prefix__/g, form_idx));
        $('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    });
    
});
function delete_formset(id){

    $("#id_form-"+id+"-DELETE").prop('checked',true);
    $("#id_form_div_form-"+id).css('display','none');
    return false;
}

function showModal(url){
    //Cerramos primero si hay otro modal
    //$("#id_modal").modal("hide")
    //$("#id_modal").remove()
    //$(".modal-backdrop").remove();
    
    //$("#id_mloading").modal("show")
    
    $.ajax({
        url: url,
        success: function(res) {
            // Pongo una espera para que se cierre sino no se cierra
            //parece un problema porque se abre y se cierra muy rapido
            
            //$("#id_mloading").modal("hide")
            //$(".modal-backdrop").remove();
            
            $("#id_container").prepend(res);
            
            $("#id_modal").modal("show");
                
            
        },
        error: function() {
            setTimeout(function(){
                $("#id_mloading").modal("hide");
            }, 500);
            console.log("No se ha podido obtener la información");
            
        },
        complete: function(){
            $("#id_mloading").modal("hide");
        }
    });
    
}
function confirmDialog(titulo,mensaje,enlace,fun=false){
    
    $("#id_modal_title").text(titulo)
    $("#id_modal_body").text(mensaje)
    if( fun==true){
        $("#id_modal_link").prop('href',"#")
        $("#id_modal_link").attr('onclick',enlace)
    }else{
        $("#id_modal_link").prop('href',enlace) 
    }
    
    $("#id_modal_confirm").modal("show")
        
}
function modificar_campo(selector,valor,fecha=false){
    if(valor!="" && valor!=null) {
        if (fecha){
            f=(valor).split('/')
            valor=f[2]+"-"+f[1]+"-"+f[0]
        }
        $(selector).val(valor)
        $(selector).css("border-color","orange")
        $(selector).parents(".collapse").collapse('show')
    }   
}
function error_campo(id_campo,mensaje){
    
    $("#div_"+id_campo+" div").append("<p class='invalid-feedback'><strong>"+mensaje+"</strong></p>")
    $("#"+id_campo).addClass("is-invalid")
    $("#"+id_campo).parents(".collapse").collapse('show')

}
function msg_info(msg,tag){
//Mensaje de información
    $("#id_container").prepend(`
    <div style="margin-top:30px;" class="alert alert-`+tag+`" role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
         </button>
        `+msg+`
    </div>`)
}
