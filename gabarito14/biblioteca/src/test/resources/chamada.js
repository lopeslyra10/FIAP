fetch('http://localhost:8080/alunos', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    nome: 'Rodrigo',
    chamada: '45332',
    turma: '1TDSPY',
    endereco: {
       cep: '01001000'
    }
  })
})
.then(response => response.text())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));