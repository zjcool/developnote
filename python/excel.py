

import xlrd
import sys
import json
import os 


data =xlrd.open_workbook('/Users/eden/Desktop/a.xlsx')
table = data.sheet_by_name(u'Sheet1')
id_cards = table.col_values(4)
yw_ids = table.col_values(6)
wifi_ids = table.col_values(7)
dic_yw=dict()
dic_wifi= dict()
for index in range(len(id_cards)):
    if index==0:
        continue
    if not str(yw_ids[index]).strip()=='':
        print 'key_yw:',yw_ids[index]
        dic_yw[yw_ids[index]]=id_cards[index]
    if not str(wifi_ids[index]).strip()=='':
        print 'key_wifi:',int(wifi_ids[index])
        dic_wifi[int(wifi_ids[index])]=id_cards[index]
yw=json.dumps(dic_yw,ensure_ascii=False,indent=4)
wifi=json.dumps(dic_wifi,ensure_ascii=False,indent=4)

f= open('./python/yw.json','w+')
f.write(str(yw))
f= open('./python/wifi.json','w+')
f.write(str(wifi))
f.close
