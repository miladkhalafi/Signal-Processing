### 🔹 **اسلاید 15 تا 17: نسبت سیگنال به نویز (SNR) و متوسط‌گیری دسته‌جمعی**



![Math Formula](<https://latex.codecogs.com/svg.latex?SNR%20%3D%2010%20%5Clog_%7B10%7D%20%5Cleft%28%20%5Cfrac%7BE_%7B%5Ctext%7Bsignal%7D%7D%7D%7BE_%7B%5Ctext%7Bnoise%7D%7D%7D%20%5Cright%29>)


#### مثال:

فرض کن:

```
Original = [-2, 0, 0, 2]
Noisy1 = [-2.2, -0.2, 0.2, 2.2]
Noise = Original - Noisy = [0.2, 0.2, -0.2, -0.2]
E_noise = 0.2^2 + 0.2^2 + 0.2^2 + 0.2^2 = 0.16
E_signal = 2^2 + 2^2 = 8
SNR = 10*log10(8/0.16) ≈ 16.99 dB
```
