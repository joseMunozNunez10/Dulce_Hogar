// Define la función para filtrar las comunas
function filtrar_comunas() {
    // Obtener el ID de la región seleccionada
    const selectedRegionId = $('#region_cod').val();
    
    // Iterar sobre todas las opciones de comunas y mostrar solo las que coinciden con el ID de la región
    $('#comuna_cod option').each(function() {
        const comuna = $(this);
        const comunaRegionId = comuna.data('region'); // Obtener el ID de la región asociado con la comuna
        
        if (selectedRegionId === '' || selectedRegionId === comunaRegionId.toString()) {
            comuna.show();
        } else {
            comuna.hide();
        }
    });
}

// Ejecutar la función filtrar_comunas al detectar cambios en la selección de región
$('#region_cod').on('change', filtrar_comunas);

// Inicializar la función al cargar la página para ocultar las comunas que no corresponden
$(document).ready(function() {
    filtrar_comunas();
});


// Función para filtrar las comunas basadas en la región seleccionada
function filtrar_comunas() {
    // Obtener el ID de la región seleccionada
    const selectedRegionId = $('#id_region').val();
    
    // Iterar sobre todas las opciones de comunas y mostrar solo las que coinciden con el ID de la región
    $('#id_comuna option').each(function() {
        const comuna = $(this);
        const comunaRegionId = comuna.data('region'); // Obtener el ID de la región asociado con la comuna
        
        if (selectedRegionId === '' || selectedRegionId === comunaRegionId.toString()) {
            comuna.show();
        } else {
            comuna.hide();
        }
    });
}

// Ejecutar la función filtrar_comunas al detectar cambios en la selección de región
$('#id_region').on('change', filtrar_comunas);

// Inicializar la función al cargar la página para ocultar las comunas que no corresponden
$(document).ready(function() {
    filtrar_comunas();
});
