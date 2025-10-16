var accion = "nuevo",
    idDocente = 0;

document.addEventListener("DOMContentLoaded", event=>{ 
    frmDocentes.addEventListener("submit", e=>{
        e.preventDefault();
        guardarDocentes();
    });
    obtenerDocentes();
});

async function guardarDocentes(){
    let datos = {
        accion,
        idDocente,
        codigo: txtCodigoDocente.value,
        nombre: txtNombreDocente.value,
        dui: txtDuiDocente.value,
        materia: txtMateriaDocente.value,
        email: txtEmailDocente.value,
        telefono: txtTelefonoDocente.value,
        direccion: txtDireccionDocente.value
    };
    let response = await fetch("/docentes",{
        method: "POST",
        body: JSON.stringify(datos),
    }), 
        respuesta = await response.json();

    if(respuesta.msg!="ok"){
        alertify.error(`Error al procesar docente: ${respuesta}`);
        return;
    }
    limpiarFormulario();
    obtenerDocentes();
}

function limpiarFormulario(){
    accion = "nuevo";
    idDocente = 0;
    txtCodigoDocente.value = "";
    txtNombreDocente.value = "";
    txtDuiDocente.value = "";
    txtMateriaDocente.value = "";
    txtEmailDocente.value = "";
    txtTelefonoDocente.value = "";
    txtDireccionDocente.value = "";
}

async function obtenerDocentes(){
    let response = await fetch("/docentes"), 
        respuesta = await response.json();
    mostrarDatosDocentes(respuesta);
}

function mostrarDatosDocentes(docentes){
    let filas = "";
    docentes.forEach(docente=>{
        filas += `
            <tr onClick='mostrarDocente(${ JSON.stringify(docente) })'>
                <td>${docente.codigo}</td>
                <td>${docente.nombre}</td>
                <td>${docente.dui}</td>
                <td>${docente.materia}</td>
                <td>${docente.email}</td>
                <td>${docente.telefono}</td>
                <td>${docente.direccion}</td>
                <td><button onClick='eliminarDocente(${ JSON.stringify(docente) }, event)' class="btn btn-danger btn-sm">ELIMINAR</button></td>
            </tr>
        `;
    });
    tblDocentes.innerHTML = filas;
}

function mostrarDocente(docente){
    accion = "modificar";
    idDocente = docente.idDocente;
    txtCodigoDocente.value = docente.codigo;
    txtNombreDocente.value = docente.nombre;
    txtDuiDocente.value = docente.dui;
    txtMateriaDocente.value = docente.materia;
    txtEmailDocente.value = docente.email;
    txtTelefonoDocente.value = docente.telefono;
    txtDireccionDocente.value = docente.direccion;
}

function eliminarDocente(docente, event){
    event.preventDefault();
    if(confirm(`Esta seguro de eliminar a ${docente.nombre}`)){
        idDocente = docente.idDocente;
        accion = "eliminar";
        guardarDocentes();
    }
}