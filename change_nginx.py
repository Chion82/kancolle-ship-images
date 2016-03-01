#coding=utf8
import json, sys, os
reload(sys)
sys.setdefaultencoding('utf8')

all_ships = json.loads(open('all_ships_info.json','r').read())
for ship_info in all_ships:
	if ship_info == None:
		continue
	if not '改' in ship_info['api_name']:
		print('api_id: ' + str(ship_info['api_id']))
		print('api_name: ' + ship_info['api_name'])
		os.system("cat ./kancolle_nginx.conf | sed s/ID_TO_REPLACE/%d/ > /usr/local/etc/nginx/servers/test.conf" % ship_info['api_id'])
		os.system("nginx -s reload")
		raw_input()
