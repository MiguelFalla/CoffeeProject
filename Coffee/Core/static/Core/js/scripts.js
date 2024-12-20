/*!
* Start Bootstrap - Business Casual v7.0.9 (https://startbootstrap.com/theme/business-casual)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-business-casual/blob/master/LICENSE)
*/
// Highlights current date on contact page
window.addEventListener('DOMContentLoaded', event => {
    const listHoursArray = document.body.querySelectorAll('.list-hours li');
    listHoursArray[new Date().getDay()].classList.add(('today'));
})

// scripts.js

document.addEventListener('DOMContentLoaded', function () {
    // Función para manejar el envío de formularios
    const contactForm = document.querySelector('.contact-form form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Evita que el formulario se envíe inmediatamente

            // Aquí podrías agregar validaciones adicionales si es necesario

            const nombre = document.getElementById('nombre').value;
            const email = document.getElementById('email').value;
            const mensaje = document.getElementById('mensaje').value;

            // Muestra un mensaje de éxito (puedes cambiarlo según tus necesidades)
            alert(`Gracias por contactarnos, ${nombre}! Te responderemos pronto.`);

            // Resetea el formulario
            contactForm.reset();
        });
    }

    // Función para mostrar un mensaje cuando la página se carga
    const showWelcomeMessage = () => {
        console.log('¡Bienvenido a CofffeLive! Esperamos que disfrutes de nuestra experiencia de café.');
    };

    showWelcomeMessage();
});

document.querySelector('#crear-publicacion-btn').addEventListener('click', async () => {
    const titulo = document.querySelector('#titulo-input').value;
    const contenido = document.querySelector('#contenido-input').value;
    const response = await fetch('/crear_publicacion/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({ titulo, contenido }),
    });
    const data = await response.json();
    if (response.ok) {
        alert('Publicación creada');
        location.reload();
    } else {
        alert(data.error);
    }
});

document.querySelectorAll('.eliminar-publicacion').forEach(button => {
    button.addEventListener('click', async () => {
        const publicacionId = button.dataset.id;
        const response = await fetch(`/eliminar_publicacion/${publicacionId}/`, {
            method: 'DELETE',
            headers: { 'X-CSRFToken': getCookie('csrftoken') },
        });
        if (response.ok) {
            alert('Publicación eliminada');
            button.closest('.publicacion').remove();
        } else {
            alert('Error al eliminar publicación');
        }
    });
});

document.querySelectorAll('.agregar-comentario').forEach(button => {
    button.addEventListener('click', async () => {
        const publicacionId = button.dataset.id;
        const contenido = button.previousElementSibling.value;
        const response = await fetch(`/crear_comentario/${publicacionId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ contenido }),
        });
        const data = await response.json();
        if (response.ok) {
            alert('Comentario agregado');
            location.reload();
        } else {
            alert(data.error);
        }
    });
});

document.querySelectorAll('.eliminar-comentario').forEach(button => {
    button.addEventListener('click', async () => {
        const comentarioId = button.dataset.id;
        const response = await fetch(`/eliminar_comentario/${comentarioId}/`, {
            method: 'DELETE',
            headers: { 'X-CSRFToken': getCookie('csrftoken') },
        });
        if (response.ok) {
            alert('Comentario eliminado');
            button.closest('li').remove();
        } else {
            alert('Error al eliminar comentario');
        }
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
