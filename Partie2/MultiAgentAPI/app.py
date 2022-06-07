from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import time
import json as agent
import Utility as expert_system
import multipleAgent as ma

app = Flask(__name__)

CORS(app,resources={r"/*": {"origins": "*", "allow_headers":{"Access-Control-Allow-Origin"}}})
app.config['CORS_HEADERS'] = 'Content-Type'

# Getting a place to visit
@app.route('/api/mas', methods=['POST'])
@cross_origin(origin='*',headers=['content-type'])
def multi_agent_system():
    expert_system.clean_results()
    facts = {}
    facts["Type"] = request.json["Type"]
    facts["Quantity"] = request.json["Quantity"]
    facts["Prix"] = request.json["Prix"]
    facts["Couleur"] = request.json["Couleur"]
    facts["Promotion"] = request.json["Promotion"]
    facts["Marque"] = request.json["Marque"]
    facts["Etat"] = request.json["Etat"]
    magasin1 = ma.Auxilary_Agents("AgentAnnexe1@ubuntu-jabber.de", "ilies")
    future_magasin1 = magasin1.start()
    future_magasin1.result() # wait for receiver agent to be prepared.

    magasin2 = ma.Auxilary_Agents("AgentAnnexe2@ubuntu-jabber.de", "ilies")
    future_magasin2 = magasin2.start()
    future_magasin2.result() # wait for receiver agent to be prepared.

    magasin3 = ma.Auxilary_Agents("AgentAnnexe3@ubuntu-jabber.de", "ilies")
    future_magasin3 = magasin3.start()
    future_magasin3.result() # wait for receiver agent to be prepared.

    main_agent = ma.Main_Agents("AgentPrincipal@ubuntu-jabber.de", "ilies")
    main_agent.send_form(facts)
    main_agent.start()

    magasin1.search_product("../Bases/formulaire.json",agent.load(open("../Bases/Agent1Products.json")),"../Bases/result1.json")
    magasin2.search_product("../Bases/formulaire.json",agent.load(open("../Bases/Agent2Products.json")),"../Bases/result2.json")
    magasin3.search_product("../Bases/formulaire.json",agent.load(open("../Bases/Agent3Products.json")),"../Bases/result3.json")

    product_names = main_agent.send_result_to_user()

    # while magasin1.is_alive() or magasin2.is_alive() or magasin3.is_alive():
    #     try:
    #         time.sleep(1)
    #     except KeyboardInterrupt:
    #         main_agent.stop()
    #         magasin1.stop()
    #         magasin2.stop()
    #         magasin3.stop()
    #         break

    return expert_system.detail_product(product_names)

@app.route('/api/au', methods=['POST'])
@cross_origin(origin='*',headers=['content-type'])
def agent_update():
    file_name = request.json["NameFile"]
    name = request.json["NameProduct"]
    quantity = request.json["NewQuantity"]

    main_agent = ma.Main_Agents("AgentPrincipal@ubuntu-jabber.de", "ilies")
    main_agent.send_bought_product_quantuty(file_name, name, quantity)
    magasin = None
    if(file_name == "../Bases/Agent1Products.json"):
        magasin = ma.Auxilary_Agents("AgentAnnexe1@ubuntu-jabber.de", "ilies")
    elif(file_name == "../Bases/Agent2Products.json"):
        magasin = ma.Auxilary_Agents("AgentAnnexe2@ubuntu-jabber.de", "ilies")
    elif(file_name == "../Bases/Agent3Products.json"):
        magasin = ma.Auxilary_Agents("AgentAnnexe3@ubuntu-jabber.de", "ilies")
    magasin.update_product()
    return jsonify("Done")

@app.route('/api/productsMagasin1', methods=['GET'])
@cross_origin(origin='*',headers=['content-type'])
def FetchShop1products():
    expert_system.clean_results()
    facts = {}
    facts["Type"] = "Doesn't matter"
    facts["Quantity"] = "Doesn't matter"
    facts["Prix"] = "Doesn't matter"
    facts["Couleur"] = "Doesn't matter"
    facts["Promotion"] = "Doesn't matter"
    facts["Marque"] = "Doesn't matter"
    facts["Etat"] = "Doesn't matter"
    main_agent = ma.Main_Agents("AgentPrincipal@ubuntu-jabber.de", "ilies")
    main_agent.send_form(facts)

    magasin1 = ma.Auxilary_Agents("AgentAnnexe1@ubuntu-jabber.de", "ilies")
    magasin1.search_product("../Bases/formulaire.json",agent.load(open("../Bases/Agent1Products.json")),"../Bases/result1.json")
    product_names = main_agent.send_result_to_user()
    return expert_system.detail_product(product_names)

@app.route('/api/productsMagasin2', methods=['GET'])
@cross_origin(origin='*',headers=['content-type'])
def FetchShop2products():
    expert_system.clean_results()
    facts = {}
    facts["Type"] = "Doesn't matter"
    facts["Quantity"] = "Doesn't matter"
    facts["Prix"] = "Doesn't matter"
    facts["Couleur"] = "Doesn't matter"
    facts["Promotion"] = "Doesn't matter"
    facts["Marque"] = "Doesn't matter"
    facts["Etat"] = "Doesn't matter"

    main_agent = ma.Main_Agents("AgentPrincipal@ubuntu-jabber.de", "ilies")
    main_agent.send_form(facts)
    magasin2 = ma.Auxilary_Agents("AgentAnnexe2@ubuntu-jabber.de", "ilies")
    magasin2.search_product("../Bases/formulaire.json",agent.load(open("../Bases/Agent2Products.json")),"../Bases/result2.json")
    product_names = main_agent.send_result_to_user()
    return expert_system.detail_product(product_names)

@app.route('/api/productsMagasin3', methods=['GET'])
@cross_origin(origin='*',headers=['content-type'])
def FetchShop3products():
    expert_system.clean_results()
    facts = {}
    facts["Type"] = "Doesn't matter"
    facts["Quantity"] = "Doesn't matter"
    facts["Prix"] = "Doesn't matter"
    facts["Couleur"] = "Doesn't matter"
    facts["Promotion"] = "Doesn't matter"
    facts["Marque"] = "Doesn't matter"
    facts["Etat"] = "Doesn't matter"

    main_agent = ma.Main_Agents("AgentPrincipal@ubuntu-jabber.de", "ilies")
    main_agent.send_form(facts)
    magasin3 = ma.Auxilary_Agents("AgentAnnexe3@ubuntu-jabber.de", "ilies")
    magasin3.search_product("../Bases/formulaire.json",agent.load(open("../Bases/Agent3Products.json")),"../Bases/result3.json")
    product_names = main_agent.send_result_to_user()
    return expert_system.detail_product(product_names)