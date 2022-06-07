import time
from spade.agent import Agent
from spade.behaviour import FSMBehaviour, State
from spade.message import Message
import json as agent

import Utility as expert_system


global received_main
global received_aux_1
global obtained_products



class Main_Agents(Agent):
        class behavior(FSMBehaviour):
                async def on_start(self):
                        pass
                async def on_end(self):
                        pass
        class sending(State):
                async def run(self):
                        agents=["AgentAnnexe1@ubuntu-jabber.de",
                        "AgentAnnexe2@ubuntu-jabber.de",
                        "AgentAnnexe3@ubuntu-jabber.de"]
                        for agent in agents:
                            msg = Message(to=agent)
                            msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative
                            msg.body = "../Bases/formulaire.json"
                            await self.send(msg)
                        time.sleep(0.5)
                        self.set_next_state("waiting")
        class waiting(State):
                async def run(self):
                        msg = await self.receive(timeout=10)
                        if msg:
                                global received_main
                                received_main = msg
                                time.sleep(0.5)
                                await self.agent.stop()
                        
                
        async def setup(self):
                fsm = self.behavior()
                fsm.add_state(name="sending", state = self.sending(), initial = True)
                fsm.add_state(name="waiting", state = self.waiting())

                fsm.add_transition(source = "sending", dest = "waiting")
                fsm.add_transition(source = "waiting", dest = "sending")

                self.add_behaviour(fsm)
        def send_form(self, facts):
                form = agent.dumps(facts, indent = 7)
                with open("../Bases/formulaire.json", "w") as outfile:
                        outfile.write(form)
        def send_bought_product_quantuty(self, file, name, quantity):
                infos = {}
                infos["file"] = file
                infos["name"] = name
                infos["quantity"] = quantity
                form = agent.dumps(infos, indent = 3)
                with open("../Bases/UpdateInfo.json", "w") as outfile:
                        outfile.write(form)
        def send_result_to_user(self):
                result = {}
                ag1 = open('../Bases/result1.json')
                products1 = agent.load(ag1)
                ag2 = open('../Bases/result2.json')
                products2 = agent.load(ag2)
                ag3 = open('../Bases/result3.json')
                products3 = agent.load(ag3)
                if (products1 != []):
                        result["magasin1"] = products1
                if (products2 != []):
                        result["magasin2"] = products2
                if (products3 != []):
                        result["magasin3"] = products3
                return result


class Auxilary_Agents(Agent):
        class behavior(FSMBehaviour):
                async def on_start(self):
                        pass
                async def on_end(self):
                        pass
        class sending(State):
                async def run(self):
                        msg = Message(to="AgentPrincipal@ubuntu-jabber.de")
                        msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative
                        msg.body = obtained_products
                        await self.send(msg)
                        
                        time.sleep(0.5)
                        # stop agent from behaviour
                        await self.agent.stop()
        class waiting(State):
                async def run(self):
                        msg = await self.receive(timeout=10)
                        if msg:
                                global received_aux_1
                                received_aux_1 = msg
                                time.sleep(0.5)
                                self.set_next_state("sending")
                        
                
        async def setup(self):
                fsm = self.behavior()
                fsm.add_state(name="sending", state = self.sending())
                fsm.add_state(name="waiting", state = self.waiting(), initial = True)

                fsm.add_transition(source = "sending", dest = "waiting")
                fsm.add_transition(source = "waiting", dest = "sending")
                
                self.add_behaviour(fsm)
        def search_product(self, facts,base_de_connaissance,agent_result):
                products = expert_system.reason(base_de_connaissance, agent.load(open(facts)))
                result = agent.dumps(products, indent = 7)
                with open(agent_result, "w") as outfile:
                        outfile.write(result)
                global obtained_products
                obtained_products = agent_result
        def update_product(self):
                infos = agent.load(open("../Bases/UpdateInfo.json"))
                expert_system.update_quantity(infos["file"], infos["name"], infos["quantity"])