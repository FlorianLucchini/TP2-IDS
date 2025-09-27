document.addEventListener('DOMContentLoaded', function() {
    const costos = JSON.parse(document.getElementById('costos-data').textContent);
    const categoriaSelect = document.getElementById('categoria');
    const precioP = document.getElementById('precio');

    categoriaSelect.addEventListener('change', function() {
        const precio = costos[this.value] || "Seleccione una categoría para ver el precio";
        precioP.textContent = precio !== undefined ? "$" + precio : precio;
    });
});
