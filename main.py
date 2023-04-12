from factory import *
from entity.user import *
from encode import *

dbms = 'mysql'

my_pool = PoolFactory.get_pool(dbms)
my_pool.connect()

my_cnx = ConnectionFactory.get_connection(dbms, my_pool)

# user
dao_user = DAOFactory.get_dao(dbms).get_dao_imp(my_cnx, 'user')

# insert
user_to_insert = User(first_name='INSERTED', last_name='INSERTED', email='some@mail.com', password=encode('password'))
dao_user.insert(user_to_insert)
print(f"\n[{user_to_insert}] – was inserted")

# delete
user_to_delete = dao_user.get_by_email('to@del.com')
dao_user.delete(user_to_delete)
print(f"[{user_to_delete}] – was deleted")

# upd
user_to_upd = dao_user.get_by_id(1)
user_to_upd.last_name("UPD")
user_to_upd.first_name("UPD")
dao_user.update(user_to_upd)
print(f"[{user_to_upd}] – was updated")

my_pool.close()
