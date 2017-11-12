import bottle
from bottle import static_file, request, error, run, template, route
from beaker.middleware import SessionMiddleware

@bottle.route('/static/<skra>')
def static_skrar(skra):
    return bottle.static_file(skra, root='./public/')

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(bottle.app(), session_opts)


products = [{"pid": 1, "name": "Vara 1", "price": 1000},
            {"pid": 2, "name": "Vara 2", "price": 2000},
            {"pid": 3, "name": "Vara 3", "price": 3000},
            {"pid": 4, "name": "Vara 4", "price": 4000}
            ]

@bottle.route('/')
def index():
    return bottle.template("index.tpl", products=products)

@bottle.route("/cart")
def cart():
    session = bottle.request.environ.get('beaker.session')
    karfa = []

    if session.get ('1'):
        vara1 = session.get ('1')
        karfa.append (vara1)

    if session.get ('2'):
        vara2 = session.get ('2')
        karfa.append ( vara2 )

    if session.get ('3'):
        vara3 = session.get ('3')
        karfa.append (vara3)

    if session.get ('4'):
        vara4 = session.get ('4')
        karfa.append (vara4)

    return bottle.template ("cart.tpl", karfa=karfa)

@bottle.route("/cart/add/<id:int>")

def add_to_cart(id):
    if id == 1:
        session = bottle.request.environ.get('beaker.session')
        session["1"] = "Vara 1"
        session.save()
        return bottle.redirect("/cart")
    if id == 2:
        session = bottle.request.environ.get('beaker.session')
        session[str(id)] = products[id - 1]["name"]
        session.save()
        return bottle.redirect("/cart")
    if id == 3:
        session = bottle.request.environ.get('beaker.session')
        session[str(id)] = products[id - 1]["name"]
        session.save()
        return bottle.redirect("/cart")
    if id == 4:
        session = bottle.request.environ.get('beaker.session')
        session[str(id)] = products[id - 1]["name"]
        session.save()
        return bottle.redirect("/cart")
    else:
        return bottle.redirect("/")

@bottle.route("/cart/remove")
def remove_from_cart():
    session = bottle.request.environ.get('beaker.session')
    session.delete()
    return bottle.redirect("/cart")





bottle.run(host='0.0.0.0',port=argv[1],debug=True,reloader=True)