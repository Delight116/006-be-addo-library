from marshmallow import ValidationError
from marshmallow import fields, validate, validates
from marshmallow_peewee import ModelSchema
from models import Client, Books, Ganre, Autors, Authors_Books
from marshmallow_peewee import Related



class ClientSchema(ModelSchema):
    first_name = fields.Str(validate=[validate.Length(min=3, max=50)])
    last_name = fields.Str(validate=[validate.Length(min=3, max=50)])
    birthday = fields.Str(validate=[validate.Regexp(regex='(\d{2})[/.-](\d{2})[/.-](\d{4})$')])
    registrate_at = fields.Str(validate=[validate.Regexp(regex='(\d{2})[/.-](\d{2})[/.-](\d{4})$')])
    is_debtor = fields.Bool(default=False,)

    class Meta:
        model = Client
class GanreSchema(ModelSchema):
    name = fields.Str(validate=[validate.Length(min=3, max=50)])

    class Meta:
        model = Ganre
class AutorSchema(ModelSchema):
    name = fields.Str(validate=[validate.Length(min=3, max=100)])

    class Meta:
        model = Autors
class BookSchema(ModelSchema):
    name = fields.Str(validate=[validate.Length(min=3, max=100)])
    ganre_id = Related(nested=GanreSchema)
    autor = Related(nested=AutorSchema)
    year = fields.Int(validate=[validate.Length(min=4, max=4)])
    publisher = fields.Str(validate=[validate.Length(min=3, max=100)])

    class Meta:
        model = Books

    @validates('autor')
    def validate_autor(self, value):
        if not Autors.filter(Autors.id == value).exists():
            raise ValidationError("Can't find author!")

    @validates('ganre_id')
    def validate_ganre(self, value):
        if not Ganre.filter(Ganre.id == value).exists():
            raise ValidationError("Can't find ganre!")

class AuthorsBooksSchema(ModelSchema):
    book_id = Related(nested=BookSchema)
    author_id = Related(nested=AutorSchema)

    @validates('book_id')
    def validate_book(self, value):
        if not Books.filter(Books.id == value).exists():
            raise ValidationError("Can't find book!")

    @validates('author_id')
    def validate_autor(self, value):
        if not Autors.filter(Autors.id == value).exists():
            raise ValidationError("Can't find author!")



authorSchema = AutorSchema()
bookSchema = BookSchema()
clientSchema = ClientSchema()
ganreShema = GanreSchema()
authorBookSchema = AuthorsBooksSchema()

