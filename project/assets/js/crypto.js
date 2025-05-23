async function fetchCryptoPrice() {
  try {
    const res = await fetch('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT');
    const data = await res.json();
    document.getElementById('btc-price').textContent = `$${parseFloat(data.price).toFixed(2)}`;
  } catch (error) {
    console.error("Ошибка:", error);
  }
}

fetchCryptoPrice();
setInterval(fetchCryptoPrice, 30000);