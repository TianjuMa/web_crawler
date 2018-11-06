import pymongo
import pprint
from bson.code import Code
# import bson


class MyDBManager:

    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient.web_cr
        self.mycol = self.mydb.movies

    def insert(self, data):
        r = self.mycol.insert_one(data)
        print(r.inserted_id, data['title'])

    def delete(self):
        return

    def update(self):
        return

    def query(self, command):
        return self.mycol.find(command)

    def test(self):
        # print(1)
        mapper = Code("""
                       function () {
                         this.details.forEach(function(z) {
                           emit(z, 1);
                         });
                       }
                       """)

        reducer = Code("""
                        function (key, values) {
                          var total = 0;
                          for (var i = 0; i < values.length; i++) {
                            total += values[i];
                          }
                          return total;
                        }
                        """)

        pipeline = [{'$group': {'_id': '$title', 'count': {'$sum': 1}}}, {'$match': {'count': {"$gt": 1}}}]

        dic = {}
        # print(self.mycol.aggregate(pipeline))
        self.mycol.find().forEach(Code('''
                    function(u) { 
                       u.forSong = self.request.db.song.find_one({}, {'_id': 1})
                       self.request.db.save(u)
                     }'''))

        # for a in self.mycol.aggregate(pipeline):
        #     for i in self.mycol.find({'title': a['_id']}):
        #         print(i['_id'])

        # print(dic)

        # print(self.mycol.find().count())
        # for a in self.mycol.find():
        #     print(a)

        # for a in self.mycol.map_reduce(mapper, reducer, "myresults"):
        #     print(a)
