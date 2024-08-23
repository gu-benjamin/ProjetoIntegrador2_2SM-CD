from flask import Flask, jsonify, make_response, request

from bd import Sensores

app = Flask('sensores')

@app.route('/sensores', methods = ['GET'])
def get_sensores():
    return jsonify(Sensores)

@app.route('/sensores/<int:id>', methods = ['GET'])
def get_sensores_by_id(id):
    for sensor in Sensores:
        if sensor.get('id') == id:
            return jsonify(sensor)
        
@app.route('/sensores', methods = ['POST'])
def create_sensor():
    sensor = request.json
    Sensores.append(sensor)
    
    return make_response( jsonify(
                        menssage = 'Dados de sensores registrados com sucesso!',
                        sensor = sensor))
    
@app.route('/sensores/<int:id>', methods = ['PUT'])
def put_sensor(id):
    sensor_atualizado = request.get_json()
    for i, sensor in enumerate(Sensores):
        if sensor.get('id') == id:
            Sensores[i].update(sensor_atualizado)
            return make_response(jsonify(menssage = 'Sensor atualizado com sucesso!',
                                 sensor = Sensores[i]))
    
@app.route('/sensores/<int:id>', methods = ['DELETE'])
def delete_sensor(id):
    for i, sensor in enumerate(Sensores):
        if sensor.get('id') == id:
            del Sensores[i]
            return make_response(jsonify(menssage = 'Sensor deletado com sucesso!'))

app.run(port=5000, host='localhost')