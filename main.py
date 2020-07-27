import random
import time
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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


for instance in session.query(User).filter(User.id):
    print(instance.sensor_id, instance.temperature)
    time.sleep(0.5)
