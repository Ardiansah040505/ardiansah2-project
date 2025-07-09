import ccxt
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime

# Fungsi untuk mengambil data historis crypto
def fetch_crypto_data(exchange, symbol='BTC/USDT', timeframe='1h', limit=100):
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

# Fungsi untuk membangun model prediksi
def build_model(data):
    # Gunakan kolom 'close' sebagai target
    X = data[['open', 'high', 'low', 'volume']]
    y = data['close']
    
    # Latih model Random Forest
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    return model

# Fungsi untuk memprediksi 10 harga berikutnya
def predict_next_prices(model, data, steps=10):
    predictions = []
    last_data = data.iloc[-1][['open', 'high', 'low', 'volume']].values.reshape(1, -1)
    
    for _ in range(steps):
        next_price = model.predict(last_data)[0]
        predictions.append(next_price)
        
        # Update input untuk prediksi berikutnya
        last_data[0][0] = last_data[0][1]  # open = high sebelumnya
        last_data[0][1] = next_price       # high = harga prediksi
        last_data[0][2] = next_price       # low = harga prediksi
        last_data[0][3] *= 1.001           # volume naik sedikit
        
    return predictions

# Fungsi untuk menghitung TP dan SL
def calculate_tp_sl(prices, tp_margin=0.05, sl_margin=0.02):
    tp = [price * (1 + tp_margin) for price in prices]
    sl = [price * (1 - sl_margin) for price in prices]
    return tp, sl

# Main function
def main():
    # Inisialisasi exchange
    exchange = ccxt.binance()
    
    # Ambil daftar semua pasangan trading yang didukung oleh Binance
    try:
        markets = exchange.load_markets()
        supported_symbols = [symbol for symbol in markets if symbol.endswith('/USDT')]
    except Exception as e:
        print(f"Error loading markets: {e}")
        return
    
    while True:
        # Tampilkan daftar cryptocurrency yang didukung
        print("\nSupported cryptocurrencies:")
        for i, symbol in enumerate(supported_symbols, 1):
            print(f"{i}. {symbol}")
        
        # Input cryptocurrency dari pengguna
        choice = input("Enter the number of the cryptocurrency you want to analyze: ")
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(supported_symbols):
                symbol = supported_symbols[choice_index]
            else:
                print("Invalid choice. Defaulting to BTC/USDT.")
                symbol = 'BTC/USDT'
        except ValueError:
            print("Invalid input. Defaulting to BTC/USDT.")
            symbol = 'BTC/USDT'
        
        # Ambil data historis cryptocurrency
        print(f"Fetching {symbol} data...")
        crypto_data = fetch_crypto_data(exchange, symbol=symbol)
        if crypto_data is None:
            continue
        
        # Bangun model prediksi
        print("Building prediction model...")
        model = build_model(crypto_data)
        
        # Prediksi 10 harga berikutnya
        print("Predicting next 10 prices...")
        predicted_prices = predict_next_prices(model, crypto_data)
        
        # Hitung TP dan SL
        tp, sl = calculate_tp_sl(predicted_prices)
        
        # Tampilkan hasil di terminal
        print("\n--- Prediction Results ---")
        print(f"Cryptocurrency: {symbol}")
        print(f"Timestamp: {datetime.now()}")
        print(f"{'No.':<5} {'Price':<10} {'TP':<10} {'SL':<10}")
        for i, (price, tp_val, sl_val) in enumerate(zip(predicted_prices, tp, sl)):
            print(f"{i+1:<5} {price:<10.6f} {tp_val:<10.6f} {sl_val:<10.6f}")
        
        # Tanya pengguna apakah ingin melanjutkan
        continue_choice = input("\nDo you want to analyze another cryptocurrency? (y/n): ").strip().lower()
        if continue_choice != 'y':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
