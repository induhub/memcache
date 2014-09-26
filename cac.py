from flask import Flask
from flask import request
from flask import render_template
from time import sleep
#import memcache
import bmemcached
mc=bmemcached.Client(('localhost:11211',),'admin','QHAmhYk3rN3X')
#import pylibmc
#mc = pylibmc.Client(["127.0.0.1"], binary=True)
#mc=memcache.Client([("127.0.0.1",11211)], debug=0)

mc.set("2", "4")
mc.set("4", "256")
app = Flask(__name__)
#cache = {2:4, 4:256}
def numtopower(number):
   total= number**number
   sleep(3)
   return total

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        submitted = str(request.form['number'])
        num = int(submitted)
        # check if available in the cache
        print mc.get(submitted)
        if mc.get(submitted):
            return mc.get(submitted)
        else:
            result = numtopower(num)
            x = mc.set(submitted, str(result))
	    print x
            return str(result)

if __name__ == '__main__':
    app.run(debug=True)
