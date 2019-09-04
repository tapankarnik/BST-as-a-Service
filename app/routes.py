from app import app
import sys
#sys.path.insert(1, '../src/bst')
#print(sys.path)
from src.bst import bst

obj = bst.BST()

@app.route('/')
@app.route('/index')
def index():
    obj2 = bst.BST()
    return 'Hello There'

@app.route('/insert')
def insert():

    #try:
    #    obj
    #except:
    #    obj = bst.BST()
    #finally:
    #global obj
    obj.insert(69)
    obj.insert(23)
    obj.insert(420)
    return str(obj.inorder(obj.root))
#return 'succes'

@app.route('/search')
def search():

    try:
        obj
    except NameError:
        return str("object not defined")
    else:
        if(obj.search(23)):
            return str("Found")
        else:
            return str("Not Found")

@app.route('/delete')
def delete():

    global obj
    try:
        obj
    except NameError:
        return str("object not defined")
    else:
        obj.delete(420, obj.root)
    return str(obj.inorder(obj.root))
        
