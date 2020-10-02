# ClientLibraryのインポート 
from virl2_client import ClientLibrary
import json

# CML2サーバのアドレス、クレデンシャル指定 
address = '10.71.158.154'

username='admin' 

password='C!sco123' 

# CML2サーバへのアクセス 

client=ClientLibrary(address,username,password,ssl_verify=False) 

#client.wait_for_lld_connected() 

print('connected') 


# import_lab
topology=open('../topology_template/template_answer.yaml', 'r')
title="answer"
#print(json.load(topology))
#print(client.import_lab(topology,title))

# Labリスト(lab_id:string)の取得 

print(client.get_lab_list()) 

# 適当に1つ目を取得 

lab_id=client.get_lab_list()[0] 

# Labにjoin、これで内部トポロジーの設定やコンポーネントを取得できる 

lab=client.join_existing_lab(lab_id,sync_lab=True) 

# pyatsのtestbed(yaml)を出力 

print(lab.get_pyats_testbed()) 

# すべてのラボを出力
all_labs_names = [lab.id for lab in client.all_labs()]
print(all_labs_names)