from flask import Flask, request, jsonify

app = Flask(__name__)

dados = []

@app.route('/tarefas', methods=['GET', 'POST'])
def tarefas():
  if request.method == 'GET':
    return jsonify(dados)
  if request.method == 'POST':
    nova_tarefa = request.get_json()
    if nova_tarefa:
      dados.extend(nova_tarefa)
      return {'mensagem': 'Nova tarefa adicionada com sucesso!'}


@app.route('/tarefas/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def tarefa(id):
  if request.method == 'GET':
    for tarefa in dados:
      if tarefa.get('id') == id:
        return jsonify(tarefa)
  if request.method == 'PUT':
    tarefa_editada = request.get_json()
    if tarefa_editada:
      for i, tarefa in enumerate(dados):
        if tarefa.get('id') == id:
          dados[i].update(tarefa_editada)
          return {'mensagem': 'Tarefa atualizada com sucesso!'}
  if request.method == 'DELETE':
    for i, tarefa in enumerate(dados):
        if tarefa.get('id') == id:
          del dados[i]
          return {'mensagem': 'Tarefa deletada com sucesso!'}

    
if __name__ == '__main__':
  app.run(debug=True)