import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'ffdf6b8895ad49d3af4db2724aea4c3b' }
connection.request('GET', '/v2/competitions/DED', None, headers )
response = json.loads(connection.getresponse().read().decode())

print(response)