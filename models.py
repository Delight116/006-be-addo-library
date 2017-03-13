import peewee as pw
import datetime as dt
db = pw.SqliteDatabase('library.db')


def initialize():
    print("Initialize")
    Client.create_table(fail_silently=True)
    Ganre.create_table(fail_silently=True)
    Books.create_table(fail_silently=True)
    Autors.create_table(fail_silently=True)
    Authors_Books.create_table(fail_silently=True)


class BaseModel(pw.Model):
    class Meta:
        database = db


class Client(BaseModel):
    first_name = pw.CharField(null=False)
    last_name = pw.CharField(null=False)
    birthday = pw.DateField(null=False)
    registrate_at = pw.DateField(default=dt.datetime.now())
    is_debtor = pw.BooleanField(default=False)

class Ganre(BaseModel):
    name = pw.CharField(max_length=100,  null=False)

class Books(BaseModel):
    name = pw.CharField(unique=True, null=False)
    ganre = pw.ForeignKeyField(Ganre)
    year = pw.IntegerField(null=False)
    publisher = pw.CharField(null=False)

class Autors(BaseModel):
    name = pw.CharField(max_length=100, null=False)

class Authors_Books(BaseModel):
    book = pw.ForeignKeyField(Books)
    author = pw.ForeignKeyField(Autors)