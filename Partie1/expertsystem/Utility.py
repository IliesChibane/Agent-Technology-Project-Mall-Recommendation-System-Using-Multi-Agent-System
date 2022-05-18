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
            else:
                return "Doesn't matter"
        else:
            return True

class Rule:
    def __init__(self, rule_name, conditions, type_result, result):
        self.rule_name = rule_name
        self.conditions = conditions 
        self.type_result = type_result
        self.result = result
        self.ignore = False

def JsonToRules(json_file):
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

def Reason(json_file, facts):
    but = json_file['but']
    is_static = False
    rules = JsonToRules(json_file)
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

def GetResults(results):
    FinalResult = []
    for i in range(len(results)):
        jsonobject = {}
        jsonobject[results[i][0]] = results[i][1]
        FinalResult.append(jsonobject)
    return FinalResult


def GetFacts(json_file):
    return [json_file["facts"]]

def GetRules(json_file):
    rules = JsonToRules(json_file)
    RulesObject = {}
    i = 1
    for rule in rules:
        RuleObject = {}
        for j in range(len(rule.conditions)):
            condition = rule.conditions[j].operator_type + " " + rule.conditions[j].operation + " " + rule.conditions[j].operation_value
            name = "condition f" if ((j+1) == len(rule.conditions)) else"condition "+ str(j+1)
            RuleObject[name] = condition
        RuleObject["result"] = rule.result
        RulesObject["Rule " + str(i)] = RuleObject
        i += 1
    return RulesObject
