function updateDispositivo() {
  var csrf_token = document.querySelector("[name=csrfmiddlewaretoken]").value;
  var url = '/clientes/att_disp/' + id.value ;

  data = new FormData();
  data.append('tipo', tipo.value);
  data.append('marca', marca.value);
  data.append('potencia', potencia.value);
  data.append('modelo', modelo.value);
  data.append('id', id.value);

  var iconeInput = document.getElementById('icone');
  if (iconeInput.files.length > 0) {
    data.append('icone', iconeInput.files[0]);
  }

  fetch(url, {
    method: 'POST',
    body: data,
    headers: {
      'X-CSRFToken': csrf_token
    },
  })
  .then(response => response.json())
  .then(data => {
    if (data.status === '200') {
      
      window.location.href = '/clientes/';
  }

    console.log(data);
  })
}
