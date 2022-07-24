# restaurant-menu

## Pages
http://127.0.0.1:8000/menu/ - the main page(menu)

http://127.0.0.1:8000/order/ - the page with your order

## API
List of all dishes:
```
curl -X GET http://127.0.0.1:8000/dishes/ -H 'Authorization: Token ce682be59d1e8b4595f6ec546d8129d11f90df7f'
```

Add new dish:
```
curl -X POST http://127.0.0.1:8000/dishes/ \
   -H 'Content-Type: application/json' -H 'Authorization: Token ce682be59d1e8b4595f6ec546d8129d11f90df7f' \
   -d '{"name": "Pork ribs", "category": 1, "allergens": [], "energy_value": 500, "price": "1000", "image": "ribs.jpeg"}'
```
