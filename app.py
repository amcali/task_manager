from flask import Flask, render_template, request, redirect, url_for

import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)# "magic code" -- boilerplate
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb://root:r00tUs3r@myfirstcluster-shard-00-00-jr2lf.mongodb.net:27017,myfirstcluster-shard-00-01-jr2lf.mongodb.net:27017,myfirstcluster-shard-00-02-jr2lf.mongodb.net:27017/task_manager?ssl=true&replicaSet=myFirstCluster-shard-0&authSource=admin&retryWrites=true&w=majority'


mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())

if __name__ == '__main__':
   app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)
