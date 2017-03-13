from flask import Flask, jsonify, request
from models import Client, Books, Ganre, Autors, Authors_Books, initialize
from playhouse.shortcuts import model_to_dict
from schemas import authorBookSchema, authorSchema, bookSchema, clientSchema, ganreShema

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    return jsonify({'status': "Ok"}), 200

# CREATE

@app.route('/api/clients', methods=['POST'])
def create_client():
    client, errors = clientSchema.load(request.json)

    if errors:
        return jsonify(errors), 400

    client.save()

    return jsonify(clientSchema.dump(client).data), 201
@app.route('/api/authors', methods=['POST'])
def create_author():
    author, errors = authorSchema.load(request.json)

    if errors:
        return jsonify(errors), 400

    author.save()

    return jsonify(authorSchema.dump(author).data), 201
@app.route('/api/books', methods=['POST'])
def create_book():
    book, errors = bookSchema.load(request.json)

    if errors:
        return jsonify(errors), 400

    book.save()

    return jsonify(bookSchema.dump(book).data), 201
@app.route('/api/ganre', methods=['POST'])
def create_ganre():
    ganre, errors = ganreShema.load(request.json)

    if errors:
        return jsonify(errors), 400

    ganre.save()

    return jsonify(ganreShema.dump(ganre).data), 201
@app.route('/api/authorbook', methods=['POST'])
def create_author_book():
    ab, errors = authorBookSchema.load(request.json)

    if errors:
        return jsonify(errors), 400

    ab.save()

    return jsonify(authorBookSchema.dump(ab).data), 201

# GET LIST

@app.route('/api/clients', methods=['GET'])
def getlist_client():
    return jsonify(clientSchema.dump(list(Client.select()), many=True).data), 200
@app.route('/api/authors', methods=['GET'])
def getlist_author():
    return jsonify(authorSchema.dump(list(Autors.select()), many=True).data), 200
@app.route('/api/books', methods=['GET'])
def getlist_book():
    return jsonify(bookSchema.dump(list(Books.select()), many=True).data), 200
@app.route('/api/ganre', methods=['GET'])
def getlist_ganre():
    return jsonify(ganreShema.dump(list(Ganre.select()), many=True).data), 200
@app.route('/api/authorbook', methods=['GET'])
def getlist_author_book():
    return jsonify(authorBookSchema.dump(list(Authors_Books.select()), many=True).data), 200

# GET ONE ELEMENT

@app.route('/api/clients/<int:id>', methods=['GET'])
def get_client(id):
    try:
        client = Client.get(id=id)
        return jsonify(clientSchema.dump(client).data), 200
    except Client.DoesNotExist:
        return jsonify({"message": "Can't find Client with id - `{id}`".format(id=id)}), 404
@app.route('/api/authors/<int:id>', methods=['GET'])
def get_author(id):
    try:
        author = Autors.get(id=id)
        return jsonify(authorSchema.dump(author).data), 200
    except Autors.DoesNotExist:
        return jsonify({"message": "Can't find authors with id - `{id}`".format(id=id)}), 404
@app.route('/api/books/<int:id>', methods=['GET'])
def get_book(id):
    try:
        book = Books.get(id=id)
        return jsonify(bookSchema.dump(book).data), 200
    except Books.DoesNotExist:
        return jsonify({"message": "Can't find book with id - `{id}`".format(id=id)}), 404
@app.route('/api/ganre/<int:id>', methods=['GET'])
def get_ganre(id):
    try:
        ganre = Ganre.get(id=id)
        return jsonify(ganreShema.dump(ganre).data), 200
    except Ganre.DoesNotExist:
        return jsonify({"message": "Can't find ganre with id - `{id}`".format(id=id)}), 404
@app.route('/api/authorbook/<int:id>', methods=['GET'])
def get_author_book(id):
    try:
        ab = Authors_Books.get(id=id)
        return jsonify(authorBookSchema.dump(ab).data), 200
    except Authors_Books.DoesNotExist:
        return jsonify({"message": "Can't find Authors_Book with id - `{id}`".format(id=id)}), 404

# UPDATE

@app.route('/api/clients/<int:id>', methods=['PUT'])
def update_client(id):
    try:
        clients = Client.get(id=id)
    except Client.DoesNotExist:
        return jsonify({"message": "Can't find Client with id - `{id}`".format(id=id)}), 404

    client, errors = clientSchema.load(request.json, instance=clients)

    if errors:
        return jsonify(errors), 400

    client.save()

    return jsonify(clientSchema.dump(client).data), 200
@app.route('/api/authors/<int:id>', methods=['PUT'])
def update_author(id):
    try:
        authors = Autors.get(id=id)
    except Autors.DoesNotExist:
        return jsonify({"message": "Can't find authors with id - `{id}`".format(id=id)}), 404

    author, errors = authorSchema.load(request.json, instance=authors)

    if errors:
        return jsonify(errors), 400

    author.save()

    return jsonify(authorSchema.dump(author).data), 200
@app.route('/api/books/<int:id>', methods=['PUT'])
def update_book(id):
    try:
        books = Books.get(id=id)
    except Books.DoesNotExist:
        return jsonify({"message": "Can't find book with id - `{id}`".format(id=id)}), 404

    book, errors = bookSchema.load(request.json, instance=books)

    if errors:
        return jsonify(errors), 400

    book.save()

    return jsonify(bookSchema.dump(book).data), 200
@app.route('/api/ganre/<int:id>', methods=['PUT'])
def update_ganre(id):
    try:
        ganre = Ganre.get(id=id)
    except Ganre.DoesNotExist:
        return jsonify({"message": "Can't find ganre with id - `{id}`".format(id=id)}), 404

    ganres, errors = ganreShema.load(request.json, instance=ganre)

    if errors:
        return jsonify(errors), 400

    ganres.save()

    return jsonify(ganreShema.dump(ganres).data), 200
@app.route('/api/authorbook/<int:id>', methods=['PUT'])
def update_author_book(id):
    try:
        ab = Authors_Books.get(id=id)

    except Authors_Books.DoesNotExist:
        return jsonify({"message": "Can't find Authors_Book with id - `{id}`".format(id=id)}), 404

    abk, errors = authorBookSchema.load(request.json, instance=ab)

    if errors:
        return jsonify(errors), 400

    abk.save()

    return jsonify(authorBookSchema.dump(abk).data), 200

# DELETE

@app.route('/api/clients/<int:id>', methods=['DELETE'])
def del_client(id):
    exists = Client.select().filter(id=id).exists()

    if not exists:
        return jsonify({"message": "Can't find client with id - `{id}`".format(id=id)}), 404

    Client.delete().where(Client.id == id).execute()
    return jsonify({}), 204
@app.route('/api/authors/<int:id>', methods=['DELETE'])
def del_author(id):
    exists = Autors.select().filter(id=id).exists()

    if not exists:
        return jsonify({"message": "Can't find author with id - `{id}`".format(id=id)}), 404

    Autors.delete().where(Autors.id == id).execute()
    return jsonify({}), 204
@app.route('/api/books/<int:id>', methods=['DELETE'])
def del_book(id):
    exists = Books.select().filter(id=id).exists()

    if not exists:
        return jsonify({"message": "Can't find book with id - `{id}`".format(id=id)}), 404

    Books.delete().where(Books.id == id).execute()
    return jsonify({}), 204
@app.route('/api/ganre/<int:id>', methods=['DELETE'])
def del_ganre(id):
    exists = Ganre.select().filter(id=id).exists()

    if not exists:
        return jsonify({"message": "Can't find ganre with id - `{id}`".format(id=id)}), 404

    Ganre.delete().where(Ganre.id == id).execute()
    return jsonify({}), 204
@app.route('/api/authorbook/<int:id>', methods=['DELETE'])
def del_author_book(id):
    exists = Authors_Books.select().filter(id=id).exists()

    if not exists:
        return jsonify({"message": "Can't find Authors_Books with id - `{id}`".format(id=id)}), 404

    Authors_Books.delete().where(Authors_Books.id == id).execute()
    return jsonify({}), 204


if __name__ == '__main__':
    initialize()
    app.run(use_reloader=True)