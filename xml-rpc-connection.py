import xmlrpc.client

url = 'http://localhost:8069'
username = 'admin'
password = 'admin'
db = 'odoo18'

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
print(common.version())
user_uid = common.authenticate(db, username, password, {})
print(user_uid)

models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# SEARCH 
# params: db, uid, pw, object, method, params
player_ids = models.execute_kw(db, user_uid, password, 'football.player', 'search', [[]], {'offset': 0, 'limit': 1}) # means start at 0 and shows only 1 record
# add a dictionary to filter records
print("search function --> ", player_ids)

# COUNT 
# params: db, uid, pw, object, method, params
count_player_ids = models.execute_kw(db, user_uid, password, 'football.player', 'search_count', [[]])
print("count function --> ", count_player_ids)

# READ 
# params: db, uid, pw, object, method, params
read_player_ids = models.execute_kw(db, user_uid, password, 'football.player', 'read', [player_ids])
read_player_name = models.execute_kw(db, user_uid, password, 'football.player', 'read', [player_ids], {'fields': ['name']})
print("read function --> ", read_player_ids)
print("read name function --> ", read_player_name)


# SEARCH AND READ
# params: db, uid, pw, object, method, params
search_read_player_ids = models.execute_kw(db, user_uid, password, 'football.player', 'search_read', [[]], {'fields':['name']})
print("search and read function --> ", search_read_player_ids)

# CREATE 
# params: db, uid, pw, object, method, params
create_player_ids = models.execute_kw(db, user_uid, password, 'football.player', 'create', [{'name':'Matheus Cunha RPC', 'sales_id': 2}]) # sales person id is an mandatory field
print("create function --> ", create_player_ids)

# WRITE/UPDATE
# params: db, uid, pw, object, method, params
write_player_ids = models.execute_kw(db, user_uid, password, 'football.player', 'write', [[8], {'name': 'Matheus Cunha RPC Updated'}])
read_name_get = models.execute_kw(db, user_uid, password, 'football.player', 'name_get', [[8]])
print("write function --> ", write_player_ids)
print("name get function --> ", read_name_get)

# DELETE/UNLINK
# params: db, uid, pw, object, method, params
unlink_player_ids = models.execute_kw(db, user_uid, password, 'football.player', 'unlink', [[8]])
print("unlink function --> ", unlink_player_ids)
