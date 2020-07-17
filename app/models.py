from app import db


class TempReading(db.Model):
    date_time = db.Column(db.Float, primary_key=True)
    temperature = db.Column(db.Float, index=True, unique=False)
    humidity = db.Column(db.Float, index=True, unique=False)

    def __repr__(self):
        return '<date_time {dt} temperature {t} humidity {h}>'.format(dt=self.temperature, t=self.temperature,
                                                                      h=self.humidity)
