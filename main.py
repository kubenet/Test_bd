import random
import time
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

engine = create_engine('sqlite:///test.db', echo=True)

Base = declarative_base()


#
# metadata = MetaData()
# users_table = Table('users', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('fullname', String),
#     Column('password', String)
# )

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    sensor_id = Column(String)
    temperature = Column(Integer)

    def __init__(self, sensor, temperature):
        self.sensor_id = sensor
        self.temperature = temperature

    def __repr__(self):
        return "<User('%s','%d')>" % (self.sensor_id, self.temperature)


# Создание таблицы
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)  # Как только у вас появится engine
session = Session()

for i in range(100):
    my_senor = User('Sens' + str(i), random.randint(25, 150))
    session.add_all([my_senor])  # добавить сразу пачку записей

session.commit()


# print(f" Имя нового пользователя {vasia_user1.name} и id: {vasia_user1.id}")

# for instance in session.query(User).filter(User.id):
#     if instance.name==vasia_user1.name:
#         print('Такая запись уже есть')
#     else:
#         #instance.name='Oleg'
#         session.add_all([vasia_user1])  # добавить сразу пачку записей
#         session.commit()
#         print(instance.name, instance.fullname, instance.password)
# print(instance)

data = np.random.rand(2, 25)

def update_line(num, data, line):
    line.set_data(data[..., :num])
    return line,


fig1 = plt.figure()
#data = np.array([1,2,3])

for instance in session.query(User).filter(User.id):
    print(instance.sensor_id, instance.temperature)
    #data = data.append(data, instance.temperature)
#
    newData = np.insert(data, float(instance.temperature))
    l, = plt.plot([], [], 'r-')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel('x')
    plt.title('test')
    line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(newData, l),
                                   interval=50, blit=True)

    plt.show()

for instance in session.query(User).filter(User.id):
    print(instance.sensor_id, instance.temperature)
    # time.sleep(0.5)


'''
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange
from threading import Thread
import time


class LiveGraph:
    def __init__(self):
        self.x_data, self.y_data = [], []
        self.figure = plt.figure()
        self.line, = plt.plot(self.x_data, self.y_data)
        self.animation = FuncAnimation(self.figure, self.update, interval=200)
        self.th = Thread(target=self.thread_f, daemon=True)
        self.th.start()

    def update(self, frame):
        self.line.set_data(self.x_data, self.y_data)
        self.figure.gca().relim()
        self.figure.gca().autoscale_view()
        return self.line,

    def show(self):
        plt.show()

    def thread_f(self):
        x = 0
        f = open('pid_current_temperatures', 'r')
        while True:
            #self.y_data.append()   
            time.sleep(0.2)
            x += 1
            data = f.readline()
            self.x_data.append(x)
            self.y_data.append(data.split(' '))
          

g = LiveGraph()
g.show()

'''