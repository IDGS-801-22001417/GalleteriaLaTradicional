// Función para abrir el modal de agregar insumos
function abrirModalAgregar() {
    // Mostrar el modal
    document.getElementById('modalAgregar').style.display = 'flex';

    // Obtener la fecha actual en formato YYYY-MM-DD
    const fechaActual = new Date();
    const fechaFormateada = fechaActual.toISOString().split('T')[0]; // Formatea a YYYY-MM-DD

    // Establecer la fecha en el campo correspondiente del modal
    document.getElementById('fechaagregar').value = fechaFormateada;

    // Aquí puedes agregar más lógica si es necesario, como cargar datos dinámicos
}

// Función para cerrar el modal de agregar insumos
function cerrarModalAgregar() {
    // Ocultar el modal
    document.getElementById('modalAgregar').style.display = 'none';
}



// Función para abrir el modal de agregar insumos
function abrirModalRegistar() {
    // Mostrar el modal
    document.getElementById('modalRegistrar').style.display = 'flex';

    // Obtener la fecha actual en formato YYYY-MM-DD
    const fechaActual = new Date();
    const fechaFormateada = fechaActual.toISOString().split('T')[0]; // Formatea a YYYY-MM-DD

    // Establecer la fecha en el campo correspondiente del modal
    document.getElementById('fechaagregar').value = fechaFormateada;

    // Aquí puedes agregar más lógica si es necesario, como cargar datos dinámicos
}

// Función para cerrar el modal de agregar insumos
function cerrarModalRegistrar() {
    // Ocultar el modal
    document.getElementById('modalRegistrar').style.display = 'none';
}