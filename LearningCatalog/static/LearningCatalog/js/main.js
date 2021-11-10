// obtener el csftoken
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function followLesson(pk){
    //Agregar impresora por medio de ajax
    fetch(`FollowLesson`, {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest', 
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'jsonBody':{"pk":pk}})  
    })
    .then(response => response.text())
    .then( text => {
       lessonLogic(text, pk)
    })
}


function lessonLogic(respuesta, pk){
    contenedor = document.getElementById('contenedor')
    if (respuesta == "follow"){
        contenedor.innerHTML = `<button class="btn btn-primary" onclick="followLesson(${pk})">
        Seguir
        <span class="material-icons-outlined align-middle">
            bookmark
        </span>
    </button>`
    }
    else{
        contenedor.innerHTML = ` <button class="btn btn-danger" onclick="followLesson(${pk})">
        Dejar de seguir
        <span class="material-icons-outlined align-middle">
            bookmark
        </span>
    </button>`
    }
}
