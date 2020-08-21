async function init () {
  const id = location.href.split('/').pop()
  const res = await fetch('/api/shops/' + id)
  const shop = await res.json()

  shopId.innerText = shop.id
  shopName.innerText = shop.name
}

window.addEventListener('load', init)
