from flask import make_response, jsonify

class Response(object):
    payload = {
        "values": None,
        "message": ""
    }

    code_status = 200

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
