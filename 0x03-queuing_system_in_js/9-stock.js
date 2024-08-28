#!/usr/bin/node
let listProducts = [
  { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function getItemById(id) {
	return listProducts.find(product=>product.Id === id);
}

function reserveStockById(itemId, stock) {

 }
async function getCurrentReservedStockById(itemId) {
	let stock = getItemById(itemId);
	return {"itemId":stock.Id, "itemName": stock.name, "price": stock.price, "initialAvailableQuantity": stock.stock};
}
