from flask import make_response, jsonify

class Response(object):
    @staticmethod
    def ok(message, values):
        return make_response(
            jsonify({
                'code_status': 200,
                'values': values,
                'message': message
            }), 
            200
        )

    @staticmethod
    def bad_request(message, values):
        return make_response(
            jsonify({
                'code_status': 400,
                'values': values,
                'message': message
            }), 
            400
        )

    @staticmethod
    def not_found(message, values):
        return make_response(
            jsonify({
                'code_status': 404,
                'values': values,
                'message': message
            }), 
            404
        )