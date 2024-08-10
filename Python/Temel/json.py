# -*- coding: utf-8 -*-
import json

data = '{"firstName" : "Erman", "lastName" : "Sezer"}'

y = json.loads(data)

print(y["firstName"])

customer = {
        "firsName" : "Serhat",
        "email" : "serhatsezer@gmail.com"
    }

customerJson = json.dumps(customer)

print(customer)

print(json.dumps("Erman"))