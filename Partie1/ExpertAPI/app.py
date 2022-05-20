from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json
import Utility as expert_system

## Init app

app = Flask(__name__)

# Opening JSON file
f1 = open('Bases/Products.json')
f2 = open('Bases/Vehicles.json')

products = json.load(f1)
vehicles = json.load(f2)

CORS(app,resources={r"/*": {"origins": "*", "allow_headers":{"Access-Control-Allow-Origin"}}})
app.config['CORS_HEADERS'] = 'Content-Type'

# Getting a place to visit
@app.route('/api/products', methods=['POST'])
@cross_origin(origin='*',headers=['content-type'])
def productsAgent():
    facts = {}
    facts["Category"] = request.json["Category"]
    facts["Type"] = request.json["Type"]
    facts["Size"] = request.json["Size"]
    facts["Function"] = request.json["Function"]
    facts["Portable"] = request.json["Portable"]
    results = expert_system.reason(products,facts)
    return jsonify(expert_system.GetResults(results))

# Getting a place to visit
@app.route('/api/vehicles', methods=['POST'])
@cross_origin(origin='*',headers=['content-type'])
def VehicleAgent():
    facts = {}
    facts["Motor"] = request.json["Motor"]
    facts["Size"] = request.json["Size"]
    facts["Vehicule_Type"] = request.json["Vehicule_Type"]
    facts["Number_of_wheels"] = request.json["Number_of_wheels"]
    facts["Number_of_doors"] = request.json["Number_of_doors"]
    results = expert_system.reason(vehicles,facts)
    return jsonify(expert_system.GetResults(results))

#Getting the facts 
@app.route('/api/VehiclesFacts', methods=['GET'])
@cross_origin(origin='*',headers=['content-type'])
def FetchFactsVehicles():
    return jsonify(expert_system.get_facts(vehicles))

@app.route('/api/productsFacts', methods=['GET'])
@cross_origin(origin='*',headers=['content-type'])
def FetchFactsproducts():
    return jsonify(expert_system.get_facts(products))

#Getting the rules
@app.route('/api/productsRules', methods=['GET'])
@cross_origin(origin='*',headers=['content-type'])
def FetchRulesproducts():
    return jsonify(expert_system.get_rules(products))

@app.route('/api/VehicleRules', methods=['GET'])
@cross_origin(origin='*',headers=['content-type'])
def FetchRulesVehicle():
    return jsonify(expert_system.get_rules(vehicles))
