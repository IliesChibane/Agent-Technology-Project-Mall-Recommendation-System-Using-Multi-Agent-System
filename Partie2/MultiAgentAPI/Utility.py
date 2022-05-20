class Condition:
    def __init__(self,operator_type, operation, operation_value):
        self.operator_type = operator_type
        self.operation  = operation
        self.operation_value = operation_value
    def compare(self, fact):
        if(fact != "Doesn't matter"):
            if(self.operation == "=="):
                return fact == self.operation_value
            elif(self.operation == "!="):
                return fact != self.operation_value
            elif(self.operation == "<"):
                return fact < self.operation_value
            elif(self.operation == ">"):
                return fact > self.operation_value
            elif(self.operation == "<="):
                return fact <= self.operation_value
            elif(self.operation == ">="):
                return fact >= self.operation_value
            elif(self.operation == "%"):
                return fact in self.operation_value
            else:
                return "Doesn't matter"
        else:
            return True
    def to_string(self):
        return self.operator_type + " " + self.operation + " " + self.operation_value

class Rule:
    def __init__(self, rule_name, conditions, type_result, result):
        self.rule_name = rule_name
        self.conditions = conditions 
        self.type_result = type_result
        self.result = result
        self.ignore = False

def json_to_rules(json_file):
    json_rules = json_file["rules"]
    jr = list(json_rules.values())
    rules = []
    for r in jr:
        conditions = []
        for c in r["AND"]:
            cond = Condition(c["type_operator"], c["operation"], c["value_operator"])
            conditions.append(cond)
        rules.append(Rule(r["THEN"]["result"], conditions, r["THEN"]["type_result"], r["THEN"]["result"]))
    return rules

def reason(json_file, facts):
    but = json_file['but']
    is_static = False;
    rules = json_to_rules(json_file)
    results = []
    
    while(is_static == False):
        for rule in rules:
            if(rule.ignore == False):
                b = True
                for cond in rule.conditions:
                    if((cond.compare(facts[cond.operator_type]) == False)):
                        b = False
                        break
                if(b == True):
                    results.append([rule.type_result, rule.result])
                    rule.ignore = True
        if(all([but in r for r in results]) == False):
            inter_result = [r for r in results if (but in r) == False]
            for ir in inter_result:
                facts[ir[0]] = ir[1]
                results.remove(ir)
        else:
            is_static = True
    return results

def get_results(results):
    FinalResult = []
    for i in range(len(results)):
        jsonobject = {}
        jsonobject[results[i][0]] = results[i][1]
        FinalResult.append(jsonobject)
    return FinalResult


def get_facts(json_file):
    return [json_file["facts"]]

def get_rules(json_file):
    rules = json_to_rules(json_file)
    rules_object = {}
    i = 1
    for rule in rules:
        rule_object = {}
        for j in range(len(rule.conditions)):
            condition = rule.conditions[j].operator_type + " " + rule.conditions[j].operation + " " + rule.conditions[j].operation_value
            name = "condition f" if ((j+1) == len(rule.conditions)) else"condition "+ str(j+1)
            rule_object[name] = condition
        rule_object["result"] = rule.result
        rules_object["Rule " + str(i)] = rule_object
        i += 1
    return rules_object

def select_shop(key):
    import json as agent
    if(key == "magasin1"):
        return agent.load(open("Bases/Agent1Products.json"))
    elif(key == "magasin2"):
        return agent.load(open("Bases/Agent2Products.json"))
    elif(key == "magasin3"):
        return agent.load(open("Bases/Agent3Products.json"))
    else:
        return {}

def detail_product(shops_result):
    list_product_shop = {}
    for k in shops_result.keys():
        list_product = {}
        mm = shops_result[k]
        products = select_shop(k)
        r = products["rules"]
        for m in mm:
            product = {}
            for vo in r[m[1]]["AND"]:
                product[vo["type_operator"]] = vo["value_operator"]
            list_product[m[1]] = product
        list_product_shop[k] = list_product
    return list_product_shop

def update_quantity(file, name, q):
    import json as agent
    products = agent.load(open(file))
    for r in products["rules"][name]["AND"]:
        if r["type_operator"] == "Quantity" :
            r["value_operator"] = str(int(r["value_operator"]) - q)
            break
    form = agent.dumps(products)
    with open(file, "w") as outfile:
        outfile.write(form)

