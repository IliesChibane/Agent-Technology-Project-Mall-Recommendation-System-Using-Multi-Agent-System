from flask import Flask,request, jsonify
from flask_cors import CORS,cross_origin
import json
import Utility as expert_system

## Init app

app = Flask(__name__)

# Opening JSON file
f1 = open('Tourism.json')
f2 = open('Vehicles.json')

tourism = json.load(f1)
vehicles = json.load(f2)

CORS(app,resources={r"/*": {"origins": "*", "allow_headers":{"Access-Control-Allow-Origin"}}})
app.config['CORS_HEADERS'] = 'Content-Type'

# Getting a place to visit
@app.route('/api/tourism', methods=['POST'])
@cross_origin(origin='*',headers=['content-type'])
def TourismAgent():
    facts = {}
    facts["Type"] = request.json["Type"]
    facts["Localisation"] = request.json["Localisation"]
    facts["Prix"] = request.json["Prix"]
    facts["Climat"] = request.json["Climat"]
    facts["Type_lieu"] = request.json["Type_lieu"]
    facts["Periode"] = request.json["Periode"]
    facts["Endroit_pour_se_detendre"] = request.json["Endroit_pour_se_detendre"]
    results = expert_system.Reason(tourism,facts)
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
    results = expert_system.Reason(vehicles,facts)
    return jsonify(expert_system.GetResults(results))

#Getting the facts 
@app.route('/api/VehiclesFacts', methods=['GET'])
@cross_origin(origin='*',headers=['content-type'])
def FetchFactsVehicles():
    return jsonify(expert_system.GetFacts(vehicles))

@app.route('/api/TourismFacts', methods=['GET'])
@cross_origin(origin='*',headers=['content-type'])
def FetchFactsTourism():
    return jsonify(expert_system.GetFacts(tourism))

#Getting the rules
@app.route('/api/TourismRules', methods=['GET'])
@cross_origin(origin='*',headers=['content-type'])
def FetchRulesTourism():
    return jsonify(expert_system.GetRules(tourism))

@app.route('/api/VehicleRules', methods=['GET'])
@cross_origin(origin='*',headers=['content-type'])
def FetchRulesVehicle():
    return jsonify(expert_system.GetRules(vehicles))
