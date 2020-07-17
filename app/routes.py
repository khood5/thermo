from app import app
from app import db
from flask import request
from app.models import TempReading
import time
import json
from flask import render_template

ERROR_MSG = "ERROR: {}"
MIN = 60
HOUR = 60*MIN
DAY = 24*HOUR

@app.route('/get/<epoch_time>')
def get(epoch_time=None):
    if epoch_time is None:
        return ERROR_MSG.format("missing time")
    reading = TempReading.query.get(epoch_time)

    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(reading.date_time))
    temp = reading.temperature
    hu = reading.humidity
    return json.dumps([{"date_time": t, "temperature": temp, "humidity": hu}])
    # return "date_time:{dt}, temperature:{t}, humidity:{h}".format(dt=t, t=temp, h=hu)


@app.route('/submit/', methods=['POST'])
def submit():
    content = request.json
    for reading in content:
        t = TempReading(date_time=time.time(),
                        temperature=reading["temperature"],
                        humidity=reading["humidity"])
        db.session.add(t)
        db.session.commit()

    return "Done"

@app.route('/')
def graph():
    temps = TempReading.query.filter(TempReading.date_time > time.time() - DAY)
    data = []
    for reading in temps:
        date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(reading.date_time))
        data.append([date_time,
                     reading.temperature,
                     reading.humidity])
    print(data)
    return render_template('index.html', data=data)
