from flask import Flask, jsonify, request
from service import bus
app = Flask(__name__)

@app.route("/")
def health_check():
    return jsonify({
        "message": "Ok",
        "code": 0
    })

@app.route("/bus")
def get_bus_info():
    route_number = request.args.get('route_number')
    station_id = request.args.get('station_id')
    if route_number is None or station_id is None:
        return jsonify({
            "message": "Need route_number or station_id",
            "code": 40001
        })
    
    bus_color = bus.get_bus_color()
    eta, stops = bus.get_bus_location(route_number)

    return jsonify({
        "message": "Ok",
        "code": 0,
        "content": {
            "esimated_time": eta,
            "a_few_stops_away": stops,
            "color": bus_color,
            "number": route_number
        }
   })