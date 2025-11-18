const inputBuscador = document.getElementById('buscador');
const tarjetas = document.querySelectorAll('.tarjeta-libro');

inputBuscador.addEventListener('keyup', (evento)=>{
    const busqueda = evento.target.value.toLowerCase().trim();

    tarjetas.forEach((tarjeta)=> {
        const titulo = tarjeta.querySelector('.titulo').textContent.toLowerCase();
        const autor = tarjeta.querySelector('.autor').textContent.toLowerCase();

        if (titulo.includes(busqueda) || autor.includes(busqueda)){
            tarjeta.style.display = "";

        } else{
            tarjeta.style.display = 'none';
        }
    })
})

function marcarLeido(boton){
    const id = boton.getAttribute('data-id');

    fetch(`/alternar_leido/${id}`, { method: 'POST' })
        .then(response => response.json())
        .then(data =>{
            if (data.exito){
                if (data.nuevo_estado){
                    boton.classList.remove('leido-no');
                    boton.classList.add('leido-si');
                } else{
                    boton.classList.remove('leido-si');
                    boton.classList.add('leido-no')
                }
            }else{
                console.error('Hubo un error al actualizar');

            }
        })
        .catch(error => console.error('Error:', error))
}