from api_instance import api

from models.shops import get_shop

import json

@api.route("/api/shops/{id}")
class Shop:
  def on_get(self, req, res, *, id):
    shop = get_shop(id)
    res.content = json.dumps(shop)
