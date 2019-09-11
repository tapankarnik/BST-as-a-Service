from app import app
import sys
from flask import request
#sys.path.insert(1, '../src/bst')
#print(sys.path)
from src.bst import bst

obj = bst.BST()

@app.route('/')
@app.route('/index')
def index():
    msg = "Hello There\nWelcome to BST-as-a-service\nGo to /insert?key=element to perform operations"
    return msg

@app.route('/insert')
def insert():

    #try:
    #    obj
    #except:
    #    obj = bst.BST()
    #finally:
    #global obj
    arg = request.args['key']
    obj.insert(arg)
    #obj.insert(69)
    #obj.insert(23)
    #obj.insert(420)
    return str(obj.inorder(obj.root))
#return 'succes'

@app.route('/search')
def search():

    #    try:
    #    obj
    #except NameError:
    #    return str("object not defined")
    #else:

    arg = request.args['key']
    if(obj.search(arg)):
        return str("Found")
    else:
        return str("Not Found")

@app.route('/delete')
def delete():

    #    global obj
    #try:
    #    obj
    #except NameError:
    #    return str("object not defined")
    #else:
    arg = request.args['key']
    obj.root=obj.delete(arg, obj.root)
    return str(obj.inorder(obj.root))
        
@app.route('/print')
def print():
    return str(obj.inorder(obj.root))
