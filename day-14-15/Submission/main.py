from flask import Flask, jsonify, request

app = Flask(__name__)

aws_services = [
    {
        "id": 1,
        "service": "Lambda"
    },
    {
        "id": 2,
        "service": "Simple Storage Service(S3)"
    }
]

# base url
@app.route('/', methods=['GET'])
def hello():
    return "Welcome to the AWS Services Simple REST API"


# /aws_services/get_all
@app.route('/aws_services/get_all', methods=['GET'])
def get_all():
    return jsonify(aws_services)


# /aws_services/<int:service_id>
@app.route('/aws_services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    service = next((service for service in aws_services if service['id'] == service_id), None)
    if service is None:
        return jsonify({'message': 'Service not found'}), 404
    return jsonify(service)


# /aws_services/add_service
@app.route('/aws_services/add_service', methods=['POST'])
def add_service():
    new_service = {
        "id": aws_services[-1]['id'] + 1,
        "service": request.json['service']
    }
    aws_services.append(new_service)
    return jsonify(new_service), 201


# /aws_services/delete_service/<int:service_id>
@app.route('/aws_services/delete_service/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    service = next((service for service in aws_services if service['id'] == service_id), None)
    if service is None:
        return jsonify({'message': 'Service not found'}), 404
    aws_services.remove(service)
    return jsonify({'message': 'Service deleted successfully'})


# /aws_services/update_service/<int:service_id>
@app.route('/aws_services/update_service/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    service = next((service for service in aws_services if service['id'] == service_id), None)    
    if service is None:
        return jsonify({'message': 'Service not found'}), 404
    service['service'] = request.json['service']
    return jsonify(service)


if __name__ == '__main__':
    app.run(debug=True)
