#
# #mongodb 修改文档----------------------------------------------------
# import pymongo
#
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client['testdb']
# col = db['testco']
# # col.create_index([('id',pymongo.ASCENDING)],unique=True)
#
# for i in range(11,15):
#     dic={
#         'id': str(i),
#         'name': 'change'
#     }
#
#     col.insert(dic)
# #
# for x in col.find():
#     print(x)
#
# col.update_one({"id":{"$regex":'11'}}, {"$set":{"name":"a"}})
#
#
#
# # 输出修改后的  "sites"  集合
# for x in col.find():
#     print(x)
# try:
#     dic={
#         'id':3,
#         'name':3
#     }
#     col.insert(dic)
# except:
#     print('id重复')


#10位时间戳转换成----------------------------------------------------
import time
timearray=1543647556
#转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
timeArray = time.localtime(timearray)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(timearray)
print(timeArray)
print(otherStyleTime)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timearray)))

