# 1. Mengimpor library yang diperlukan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 2. Membuat dataset sintetis
np.random.seed(42)  # Untuk hasil yang konsisten
ukuran_rumah = np.random.randint(50, 200, 100)  # Ukuran rumah antara 50-200 m²
harga_rumah = ukuran_rumah * 5 + np.random.normal(0, 50, 100)  # Harga = 5 * ukuran + noise

# Membuat DataFrame
data = pd.DataFrame({'Ukuran_Rumah': ukuran_rumah, 'Harga_Rumah': harga_rumah})

# 3. Memvisualisasikan data
plt.scatter(data['Ukuran_Rumah'], data['Harga_Rumah'], color='blue')
plt.title('Hubungan Ukuran Rumah dan Harga Rumah')
plt.xlabel('Ukuran Rumah (m²)')
plt.ylabel('Harga Rumah (juta rupiah)')
plt.show()

# 4. Membagi data menjadi training dan testing
X = data[['Ukuran_Rumah']]  # Variabel independen
y = data['Harga_Rumah']     # Variabel dependen
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Melatih model regresi linear
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Memprediksi harga rumah pada data testing
y_pred = model.predict(X_test)

# 7. Menampilkan koefisien dan intercept
print(f"Koefisien: {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")

# 8. Evaluasi model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse:.2f}")

# 9. Memvisualisasikan hasil prediksi
plt.scatter(X_test, y_test, color='blue', label='Data Aktual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Prediksi')
plt.title('Prediksi Harga Rumah')
plt.xlabel('Ukuran Rumah (m²)')
plt.ylabel('Harga Rumah (juta rupiah)')
plt.legend()
plt.show()
