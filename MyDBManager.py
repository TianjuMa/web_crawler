import pymongo
from bson import code, objectid


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

    def fetch_movies(self, id=None):
        if id is None:
            return [a['title'] for a in self.mycol.find()]

        li = []

        command = {'_id': objectid.ObjectId(id)}
        for item in self.mycol.find(command):
            dic = {
                'title': item['title'],
                'img': item['img'],
                'rate': item['rate'],
                'comments': item['details']
            }

            li.append(dic)

        return li

    def removeDups(self):

        pipeline = [{'$group': {'_id': '$title', 'dups': {'$push': "$_id"}, 'count': {'$sum': 1}}},
                    {'$match': {'count': {"$gt": 1}}}]

        for a in self.mycol.aggregate(pipeline):
            l = a['dups']
            for i in range(1, len(l)):
                print(l[i])
                self.mycol.delete_one({'_id': l[i]})
