from MyDBManager import *

db = MyDBManager()

command = '[{$group:{_id:"$title", count:{$sum:1}}}, {$match:{count:{"$gt":1}}}]'

# print(db.query({'title': '楚门的世界'}).id)
db.removeDups()
