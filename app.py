from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/npcf-policyauthorization/v1/app-sessions', methods=['POST'])
def app_sessions():
    # Get JSON data from the request
    request_data = request.get_json()

    # Process the request and generate a response
    response_data = {
        "ascReqData": {
            "afAppId": request_data.get("afAppId", ""),
            "afChargId": request_data.get("afChargId", ""),
            "afReqData": request_data.get("afReqData", ""),
            "afRoutReq": {
                "appReloc": True,
                "routeToLocs": [
                    {
                        "dnai": "string",
                        "routeInfo": {
                            "ipv4Addr": "198.51.100.1",
                            "ipv6Addr": "2001:db8:85a3::8a2e:370:7334",
                            "portNumber": 0
                        },
                        "routeProfId": "string"
                    },
                    # Add more routeToLocs as needed
                ]
            }
        }
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

