# nested dictionary list,tuple,set,dict
from pprint import pprint
emps = {
    'chandu': {
        'name': 'Chandu Sharma',
        'salary': 15000,
        'designation': 'foreman'
     },
     'rohit': {
        'name' : 'Rohit Shetty',
        'salary' :'10000',
        'designation' : 'Assistant 2',
        'manager':'Ravi Prakash'
     },
     'bhanu': {
        'name' : 'Bhanu Pratap',
        'salary': '30000',
        'designation': 'system officer',
     }
}    

pprint(emps)

print("designation", emps['chandu']['designation'])

for key,data in emps.items():
    print(key, "⤵️")
    for k, v in data.items():
        print(k, v)
    print('--'*10)   
