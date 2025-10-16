var accion = "nuevo",
    idMateria = 0;

document.addEventListener("DOMContentLoaded", event=>{ 
    frmMaterias.addEventListener("submit",e=>{
        e.preventDefault();
        guardarMaterias();
    });
    obtenerMaterias();
});

async function guardarMaterias(){
    let datos = {
        accion,
        idMateria,
        uv: txtUvMateria.value,
        nombre: txtNombreMateria.value,
        docente: txtDocenteMateria.value
    };
    let response = await fetch("/materias",{
        method: "POST",
        body: JSON.stringify(datos),
    }), 
        respuesta = await response.json();
    if(respuesta.msg!="ok"){
        alertify.error(`Error al procesar materia: ${respuesta}`);
        return;
    }
    limpiarFormulario();
    obtenerMaterias();
}

function limpiarFormulario(){
    accion = "nuevo";
    idMateria = 0;
    txtUvMateria.value = "";
    txtNombreMateria.value = "";
    txtDocenteMateria.value = "";
}

async function obtenerMaterias(){
    let response = await fetch("/materias"), 
        respuesta = await response.json();
    mostrarDatosMaterias(respuesta);
}

function mostrarDatosMaterias(materias){
    let filas = "";
    materias.forEach(materia=>{
        filas += `
            <tr onClick='mostrarMateria(${ JSON.stringify(materia) })'>
                <td>${materia.uv}</td>
                <td>${materia.nombre}</td>
                <td>${materia.docente}</td>
                <td><button onClick='eliminarMateria(${ JSON.stringify(materia) }, event)' class="btn btn-danger btn-sm">ELIMINAR</button></td>
            </tr>
        `;
    });
    tblMaterias.innerHTML = filas;
}

function mostrarMateria(materia){
    accion = "modificar";
    idMateria = materia.idMateria;
    txtUvMateria.value = materia.uv;
    txtNombreMateria.value = materia.nombre;
    txtDocenteMateria.value = materia.docente;
}

function eliminarMateria(materia, event){
    event.preventDefault();
    if(confirm(`Esta seguro de eliminar a ${materia.nombre}`)){
        idMateria = materia.idMateria;
        accion = "eliminar";
        guardarMaterias();
    }
}