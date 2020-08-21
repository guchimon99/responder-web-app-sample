from api_instance import api

@api.route("/")
def home(req, res):
  res.content = api.template('home.html')

@api.route("/shops/{id}")
def shop_detail(req, res, *, id):
  res.content = api.template('shop.html', id=id)
