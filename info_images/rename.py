import json, os

ship_info = json.loads(open('ship_info.json', 'r').read())

for ship in ship_info:
	file_ext = ship['file_name'][ship['file_name'].rfind('.'):]
	try:
		os.rename(ship['file_name'].encode('utf8'), (ship['ship_no'] + file_ext).encode('utf8'))
	except Exception:
		pass

