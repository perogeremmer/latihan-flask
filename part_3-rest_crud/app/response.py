from flask import make_response, jsonify

class Response(object):
    
    __instance = None

    def __new__(cls):
        if Response.__instance is None:
            Response.__instance = object.__new__(cls)
        return Response.__instance

    def __init__(self):
        self.code_status = 200
        
        self.payload = {
            "values": None,
            "message": ""
        }

    def create_payload_response(self, message, values):
        self.payload["values"] = values
        self.payload["message"] = message

        return make_response(jsonify(self.payload), self.code_status)

    def ok(self, message, values):
        return self.create_payload_response(message, values)

    def bad_request(self, message, values):
        self.code_status = 400

        return self.create_payload_response(message, values)

    def not_found(self, message, values):
        self.code_status = 404

        return self.create_payload_response(message, values)

response = Response()