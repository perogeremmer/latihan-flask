from flask import make_response, jsonify

class Response(object):
    
    __instance = None

    def __new__(cls):
        if Response.__instance is None:
            Response.__instance = object.__new__(cls)
        return Response.__instance

    def __init__(self):
        self.status_code = None
        
        self.payload = {
            "values": None,
            "message": "",
        }

    def create_payload_response(self, message, values):
        self.payload["values"] = values
        self.payload["message"] = message
        self.payload["status_code"] = self.status_code


        return make_response(jsonify(self.payload), self.status_code)

    def ok(self, message, values):
        self.status_code = 200

        return self.create_payload_response(message, values)

    def bad_request(self, message, values):
        self.status_code = 400

        return self.create_payload_response(message, values)

    def not_found(self, message, values):
        self.status_code = 404

        return self.create_payload_response(message, values)

    def un_authorized(self, message, values):
        self.status_code = 401

        return self.create_payload_response(message, values)

response = Response()