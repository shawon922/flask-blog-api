from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser
from flask_mysqldb import MySQL

app = Flask(__name__)
api = Api(app, prefix='/api/v1')

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb_blog_api'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

article_request_parser = RequestParser(bundle_errors=True)

article_request_parser.add_argument('title', type=str, required=True, help='Title must be string')
article_request_parser.add_argument('content', type=str, required=True, help='Content must be string')


class ArticleCollection(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT id, title, content FROM articles''')
        articles = cur.fetchall()

        return make_response(jsonify(articles), 200)

    def post(self):
        args = article_request_parser.parse_args()
        cur = mysql.connection.cursor()
        query = '''INSERT INTO articles (title, content) VALUES ('{title}', '{content}')'''.format(**args)

        cur.execute(query)
        cur.connection.commit()
        return { 'msg': 'New article created.', 'data': args }, 201


class Article(Resource):
    def get(self, id):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT id, title, content FROM articles WHERE id = {id}'''.format(id=id))
        article = cur.fetchone()
        if not article:
            return { 'error': 'article not found of id {id}'.format(id=id) }
        return article, 200

    def put(self, id):
        args = article_request_parser.parse_args()
        cur = mysql.connection.cursor()
        query = '''UPDATE articles SET title = '{title}', content = '{content}' WHERE id = {id}'''.format(**args, id=id)
        cur.execute(query)
        cur.connection.commit()

        return { 'msg': 'Article updated.', 'data': args }, 200

    def delete(self, id):
        cur = mysql.connection.cursor()
        query = '''DELETE FROM articles WHERE id = {id}'''.format(id=id)
        cur.execute(query)
        cur.connection.commit()

        return { 'msg': 'Article Deleted' }, 202

api.add_resource(ArticleCollection, '/articles/')
api.add_resource(Article, '/articles/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
