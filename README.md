# flask-blog-api
## A simple API built with "flask", "flask-restful" and "flask-mysqldb".

#### Tutorial Reference
[REST API Best Practices: Python & Flask Tutorial - Polyglot.Ninja()](http://polyglot.ninja/rest-api-best-practices-python-flask-tutorial/)

###  Requirements
    Flask==0.12.1
    Flask-MySQLdb==0.2.0
    Flask-RESTful==0.3.5


### To create an article:

```
$ curl -H "Content-Type: application/json" -X POST -d '{"title": "This is title", "content": "This is content"}' http://127.0.0.1:5000/api/v1/articles/9
```

### To get all articles:

```
$ curl -X GET http://127.0.0.1:5000/api/v1/articles/
```

### To get a single article:

```
$ curl -X GET http://127.0.0.1:5000/api/v1/articles/1
```

### To update an article:

```
$ curl -H "Content-Type: application/json" -X PUT -d '{"title": "This is title", "content": "This is content"}' http://127.0.0.1:5000/api/v1/articles/9
```

### To delete an article:

```
$ curl -X DELETE http://127.0.0.1:5000/api/v1/articles/8
```
