
function rellenarCampos(){
    var campos=$("#txtaData").val().split(String.fromCharCode(9));
    //console.log(campos);
    
    $("#id_cto").val(campos[3]);
    $("#id_provincia").val(campos[4]);
    //Poblacion es lo mismo que la ciudad
    $("#id_poste_central").val(campos[6]);
    $("#id_comentarios").val(campos[7]);
    $("#id_tipo_via").val(campos[8]);
    $("#id_via").val(campos[9]);
    $("#id_numero_via").val(campos[10]);
    $("#id_nombre").val(campos[11]);
    
    $("#id_ciudad").val(campos[13]);
    var f=campos[14].split('/');
    if( f[2].length>2){
        var fecha= f[2]+"-"+f[1]+"-"+f[0];
    }else{
        var fecha= "20"+f[2]+"-"+f[1]+"-"+f[0];
    } 
   
    $("#id_fecha_ar").val(fecha);
    $("#id_car_ftth_iua").val(campos[15]);
    
    var nombretc=campos[16];
    var nombret=nombretc.split(",")[1];
    var apellido1t=nombretc.split(",")[0].split(" ")[0];
    var apellido2t=nombretc.split(",")[0].split(" ")[1];
    
    $("#id_nombre_tecnico").val(nombret);
    $("#id_apellido_tecnico").val(apellido1t);
    $("#id_segundo_apellido_tecnico").val(apellido2t);
    $("#id_dni_tecnico").val(campos[17]);
    
}

function comprobarPoste(event){
    var poste=event.target.value;
    $.ajax({
        url: "/registro/comprobar_poste/"+event.target.value, 
        success: function(result){
            if(result.poste_registrado){
                error_campo(event.target.id,"Poste ya registrado "+ result.codigo_suc);
                
            }else{
                //Ponemos el borde del poste en verde
                mensaje_campo(event.target.id,"Ok")
            }
            
        }
    
    });
    
}

function obtenerCentral(){
    var codigo=event.target.value;
    $.ajax({
        url: "/central/obtener_central/"+event.target.value, 
        success: function(result){
            if(result.encontrada){
                modificar_campo("#id_nombre_central",result.nombre_central,
                 false, "green")
                
                mensaje_campo("id_codigo_miga","Ok",
                 color="green")
            }else{
                //Ponemos el borde del poste en verde
                 mensaje_campo("id_codigo_miga","Codigo MIGA no encontrado",
                 color="orange")
            }
            
        }
    
    });
    
}
