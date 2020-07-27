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
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)


# Создание таблицы
#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)  # Как только у вас появится engine
session = Session()

vasia_user1 = User("Sergey", "S.", "8888")

#session.add_all( [vasia_user1] )   #добавить сразу пачку записей
#session.commit()
#print(f" Имя нового пользователя {vasia_user1.name} и id: {vasia_user1.id}")

for instance in session.query(User).filter(User.id):
    if instance.name==vasia_user1.name:
        print('Такая запись уже есть')
    else:
        #instance.name='Oleg'
        session.add_all([vasia_user1])  # добавить сразу пачку записей
        session.commit()
        print(instance.name, instance.fullname, instance.password)
print(instance)