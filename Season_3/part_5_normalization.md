برای **نرمال‌سازی سیگنال‌ها** به گونه‌ای که **میانگین آن‌ها صفر شود و انحراف معیارشان یک شود**، از روشی استفاده می‌کنیم که به آن **نرمال‌سازی Z-score (Standardization)** می‌گویند.

---

## 🔹 هدف:
تبدیل سیگنال به صورتی که:

- **میانگین = 0**
- **انحراف معیار = 1**

---

## 🔹 فرمول نرمال‌سازی دستی:



![Math Formula](<https://latex.codecogs.com/svg.latex?x_%7B%5Ctext%7Bnormalized%7D%7D%5Bn%5D%20%3D%20%5Cfrac%7Bx%5Bn%5D%20-%20%5Cbar%7Bx%7D%7D%7B%5Csigma_x%7D>)


که در آن:
- ![Math](<https://latex.codecogs.com/svg.latex?x%5Bn%5D>): مقدار اصلی nام سیگنال
- ![Math](<https://latex.codecogs.com/svg.latex?%5Cbar%7Bx%7D>): میانگین سیگنال
- ![Math](<https://latex.codecogs.com/svg.latex?%5Csigma_x>): انحراف معیار سیگنال

---

## 💡 مثال عددی:

فرض کنید سیگنال زیر را داریم:



![Math Formula](<https://latex.codecogs.com/svg.latex?x%20%3D%20%5B7%2C%206%2C%205%5D>)


### مرحله ۱: محاسبه میانگین



![Math Formula](<https://latex.codecogs.com/svg.latex?%5Cbar%7Bx%7D%20%3D%20%5Cfrac%7B7%20%2B%206%20%2B%205%7D%7B3%7D%20%3D%20%5Cfrac%7B18%7D%7B3%7D%20%3D%206>)


### مرحله ۲: محاسبه انحراف معیار

ابتدا تفاوت هر مقدار با میانگین و مجذور آن را پیدا می‌کنیم:

| ![Math](<https://latex.codecogs.com/svg.latex?x%5Bn%5D>) | ![Math](<https://latex.codecogs.com/svg.latex?x%5Bn%5D%20-%20%5Cbar%7Bx%7D>) | ![Math](<https://latex.codecogs.com/svg.latex?%28x%5Bn%5D%20-%20%5Cbar%7Bx%7D%29%5E2>) |
|------------|------------------------|----------------------------|
| 7          | 1                      | 1                          |
| 6          | 0                      | 0                          |
| 5          | -1                     | 1                          |

جمع مجذورات:


![Math Formula](<https://latex.codecogs.com/svg.latex?%5Csum%20%28x%5Bn%5D%20-%20%5Cbar%7Bx%7D%29%5E2%20%3D%201%20%2B%200%20%2B%201%20%3D%202>)


چون این داده‌ها یک **نمونه (Sample)** هستند (نه تمام جامعه)، از ![Math](<https://latex.codecogs.com/svg.latex?N%20-%201%20%3D%202>) استفاده می‌کنیم:



![Math Formula](<https://latex.codecogs.com/svg.latex?s%5E2%20%3D%20%5Cfrac%7B2%7D%7B2%7D%20%3D%201%20%5CRightarrow%20s%20%3D%20%5Csqrt%7B1%7D%20%3D%201>)


پس:
- میانگین = 6
- انحراف معیار = 1

### مرحله ۳: نرمال‌سازی دستی

حال هر مقدار را طبق فرمول نرمال‌سازی تغییر می‌دهیم:



![Math Formula](<https://latex.codecogs.com/svg.latex?x_%7B%5Ctext%7Bnormalized%7D%7D%5Bn%5D%20%3D%20%5Cfrac%7Bx%5Bn%5D%20-%206%7D%7B1%7D>)


محاسبه برای هر عنصر:

| ![Math](<https://latex.codecogs.com/svg.latex?x%5Bn%5D>) | ![Math](<https://latex.codecogs.com/svg.latex?x%5Bn%5D%20-%206>) | ![Math](<https://latex.codecogs.com/svg.latex?x_%7B%5Ctext%7Bnormalized%7D%7D%5Bn%5D>) |
|------------|----------------|-------------------------------|
| 7          | 1              | 1                             |
| 6          | 0              | 0                             |
| 5          | -1             | -1                            |

### ✅ نتیجه نهایی:

سیگنال نرمال‌شده:



![Math Formula](<https://latex.codecogs.com/svg.latex?x_%7B%5Ctext%7Bnormalized%7D%7D%20%3D%20%5B1%2C%200%2C%20-1%5D>)


---

## 📌 خواص سیگنال نرمال‌شده:

| ویژگی | مقدار |
|--------|--------|
| میانگین | 0 |
| انحراف معیار | 1 |
| مقادیر | حول صفر قرار گرفته‌اند و واحد بدون بعد شده‌اند |

---

## 🧠 چرا این کار را انجام می‌دهیم؟

در بسیاری از تحلیل‌های سیگنال (مثل PCA، ICA، شبکه‌های عصبی، ...) لازم است داده‌ها نرمال شوند. این کار:

- مقایسه بین ویژگی‌های مختلف را آسان‌تر می‌کند.
- اثر واحدهای مختلف (مثلاً ولت و میلی‌ولت) را حذف می‌کند.
- عملکرد الگوریتم‌ها را بهبود می‌دهد.

---

## ✅ خلاصه

روند نرمال‌سازی یک سیگنال شامل مراحل زیر است:

1. **محاسبه میانگین**
2. **محاسبه انحراف معیار**
3. **کم کردن میانگین از هر نقطه**
4. **تقسیم هر نقطه بر انحراف معیار**

