## 🔹 بخش 4: **انحراف معیار (Standard Deviation)**

### 📌 تعریف:
جذر واریانس است و واحد داده‌ها را حفظ می‌کند.

### ✅ فرمول:



![Math Formula](<https://latex.codecogs.com/svg.latex?%5Csigma%20%3D%20%5Csqrt%7B%5Csigma%5E2%7D%2C%20%5Cquad%20s%20%3D%20%5Csqrt%7Bs%5E2%7D>)


### 💡 ادامه مثال:

از قبل داشتیم:
- واریانس جامعه: ![Math](<https://latex.codecogs.com/svg.latex?%5Csigma%5E2%20%3D%200.6667>)
- واریانس نمونه: ![Math](<https://latex.codecogs.com/svg.latex?s%5E2%20%3D%201>)

پس:

- انحراف معیار جامعه:  


![Math Formula](<https://latex.codecogs.com/svg.latex?%5Csigma%20%3D%20%5Csqrt%7B0.6667%7D%20%5Capprox%200.816>)


- انحراف معیار نمونه:  


![Math Formula](<https://latex.codecogs.com/svg.latex?s%20%3D%20%5Csqrt%7B1%7D%20%3D%201>)


✅ پس انحراف معیار:
- جامعه: **0.816**
- نمونه: **1**

---

## 🔹 بخش 5: **همبستگی (Correlation)**

### 📌 تعریف:
همبستگی نشان‌دهنده شباهت خطی بین دو سیگنال است. عددی بین ![Math](<https://latex.codecogs.com/svg.latex?-1>) تا ![Math](<https://latex.codecogs.com/svg.latex?%2B1>).

### ✅ فرمول:



![Math Formula](<https://latex.codecogs.com/svg.latex?r_%7Bxy%7D%20%3D%20%5Cfrac%7B%5Ctext%7BCov%7D%28x%2C%20y%29%7D%7B%5Csigma_x%20%5Ccdot%20%5Csigma_y%7D>)


که:
- ![Math](<https://latex.codecogs.com/svg.latex?%5Ctext%7BCov%7D%28x%2C%20y%29>): کواریانس بین دو سیگنال
- ![Math](<https://latex.codecogs.com/svg.latex?%5Csigma_x%2C%20%5Csigma_y>): انحراف معیار هر سیگنال

### 💡 مثال:

فرض کنید دو سیگنال داریم:



![Math Formula](<https://latex.codecogs.com/svg.latex?x%20%3D%20%5B1%2C%202%2C%203%5D%2C%20%5Cquad%20y%20%3D%20%5B2%2C%204%2C%206%5D>)


میانگین‌ها:


![Math Formula](<https://latex.codecogs.com/svg.latex?%5Cbar%7Bx%7D%20%3D%202%2C%20%5Cquad%20%5Cbar%7By%7D%20%3D%204>)


تفاوت‌ها:


![Math Formula](<https://latex.codecogs.com/svg.latex?%28x%20-%20%5Cbar%7Bx%7D%29%20%3D%20%5B-1%2C%200%2C%201%5D%2C%20%5Cquad%20%28y%20-%20%5Cbar%7By%7D%29%20%3D%20%5B-2%2C%200%2C%202%5D>)


ضرب تفاوت‌ها:


![Math Formula](<https://latex.codecogs.com/svg.latex?%28-1%29%28-2%29%20%3D%202%2C%20%5Cquad%20%280%29%280%29%20%3D%200%2C%20%5Cquad%20%281%29%282%29%20%3D%202>)


جمع ضرب‌ها:


![Math Formula](<https://latex.codecogs.com/svg.latex?%5Csum%20%28x%20-%20%5Cbar%7Bx%7D%29%28y%20-%20%5Cbar%7By%7D%29%20%3D%202%20%2B%200%20%2B%202%20%3D%204>)


تقسیم بر ![Math](<https://latex.codecogs.com/svg.latex?N-1%20%3D%202>):


![Math Formula](<https://latex.codecogs.com/svg.latex?%5Ctext%7BCov%7D%28x%2C%20y%29%20%3D%20%5Cfrac%7B4%7D%7B2%7D%20%3D%202>)


انحراف معیار:
- ![Math](<https://latex.codecogs.com/svg.latex?%5Csigma_x%20%3D%201>), ![Math](<https://latex.codecogs.com/svg.latex?%5Csigma_y%20%3D%202>)

همبستگی:


![Math Formula](<https://latex.codecogs.com/svg.latex?r_%7Bxy%7D%20%3D%20%5Cfrac%7B2%7D%7B1%20%5Ccdot%202%7D%20%3D%201>)


✅ بنابراین همبستگی بین x و y برابر **1** است (یعنی کاملاً مثبت)

---

## 🔹 بخش 6: **PCA (تحلیل مؤلفه‌های اصلی)**

### 📌 هدف:
کاهش بعد داده‌ها با حفظ بیشترین اطلاعات (واریانس).

### ✅ مراحل محاسبه (دستی):

1. **مرکز کردن داده‌ها**: میانگین هر ستون را از مقادیر کم کن.
2. **محاسبه ماتریس کواریانس**.
3. **محاسبه مقادیر ویژه (Eigenvalues) و بردارهای ویژه (Eigenvectors)**.
4. **انتخاب k تا از بزرگترین مقادیر ویژه**.
5. **تصحیح داده‌ها روی این k مؤلفه**.

### 💡 مثال ساده:

فرض کنید داریم:



![Math Formula](<https://latex.codecogs.com/svg.latex?X%20%3D%20%5Cbegin%7Bbmatrix%7D%0A1%20%26%202%20%5C%5C%0A3%20%26%204%20%5C%5C%0A5%20%26%206%0A%5Cend%7Bbmatrix%7D>)


#### ۱. میانگین ستون‌ها:


![Math Formula](<https://latex.codecogs.com/svg.latex?%5Cbar%7Bx%7D_1%20%3D%20%5Cfrac%7B1%2B3%2B5%7D%7B3%7D%20%3D%203%2C%20%5Cquad%20%5Cbar%7Bx%7D_2%20%3D%20%5Cfrac%7B2%2B4%2B6%7D%7B3%7D%20%3D%204>)


#### ۲. مرکز کردن:


![Math Formula](<https://latex.codecogs.com/svg.latex?X_m%20%3D%20%5Cbegin%7Bbmatrix%7D%0A1-3%20%26%202-4%20%5C%5C%0A3-3%20%26%204-4%20%5C%5C%0A5-3%20%26%206-4%0A%5Cend%7Bbmatrix%7D%20%3D%0A%5Cbegin%7Bbmatrix%7D%0A-2%20%26%20-2%20%5C%5C%0A0%20%26%200%20%5C%5C%0A2%20%26%202%0A%5Cend%7Bbmatrix%7D>)


#### ۳. ماتریس کواریانس:


![Math Formula](<https://latex.codecogs.com/svg.latex?C%20%3D%20%5Cfrac%7B1%7D%7BN-1%7D%20X_m%5ET%20X_m%20%3D%20%5Cfrac%7B1%7D%7B2%7D%20%5Cbegin%7Bbmatrix%7D%0A8%20%26%208%20%5C%5C%0A8%20%26%208%0A%5Cend%7Bbmatrix%7D%20%3D%0A%5Cbegin%7Bbmatrix%7D%0A4%20%26%204%20%5C%5C%0A4%20%26%204%0A%5Cend%7Bbmatrix%7D>)


#### ۴. مقادیر ویژه:
معادله مشخصه:


![Math Formula](<https://latex.codecogs.com/svg.latex?%5Cdet%28C%20-%20%5Clambda%20I%29%20%3D%200%20%5CRightarrow%20%284-%5Clambda%29%5E2%20-%2016%20%3D%200%20%5CRightarrow%20%5Clambda_1%20%3D%208%2C%20%5C%3B%20%5Clambda_2%20%3D%200>)


#### ۵. بردار ویژه:
برای ![Math](<https://latex.codecogs.com/svg.latex?%5Clambda_1%20%3D%208>):


![Math Formula](<https://latex.codecogs.com/svg.latex?v_1%20%3D%20%5Cbegin%7Bbmatrix%7D%201%20%5C%5C%201%20%5Cend%7Bbmatrix%7D>)


#### ۶. تصحیح داده‌ها:


![Math Formula](<https://latex.codecogs.com/svg.latex?Z%20%3D%20X_m%20%5Ccdot%20v_1%20%3D%20%5B-4%2C%200%2C%204%5D%5ET>)


✅ بنابراین PCA یک بعد از دو بعد کاست و فقط مؤلفه مهم را نگه داشت.

---

## 🔹 بخش 7: **ICA (تحلیل مؤلفه‌های مستقل)**

### 📌 هدف:
جداسازی منابع مستقل از سیگنال‌های آمیخته (Blind Source Separation).

### ✅ ایده اصلی:

اگر داشته باشیم:



![Math Formula](<https://latex.codecogs.com/svg.latex?x%20%3D%20A%20%5Ccdot%20s>)


که:
- ![Math](<https://latex.codecogs.com/svg.latex?x>): سیگنال‌های آمیخته
- ![Math](<https://latex.codecogs.com/svg.latex?A>): ماتریس اختلاط
- ![Math](<https://latex.codecogs.com/svg.latex?s>): منابع اصلی (ناشناس)

هدف یافتن ![Math](<https://latex.codecogs.com/svg.latex?W%20%3D%20A%5E%7B-1%7D>) است تا بتوانیم:



![Math Formula](<https://latex.codecogs.com/svg.latex?s%20%3D%20W%20%5Ccdot%20x>)


### 💡 مثال ساده:

فرض کنید:



![Math Formula](<https://latex.codecogs.com/svg.latex?x%20%3D%20%5Cbegin%7Bbmatrix%7D%204%20%5C%5C%206%20%5C%5C%208%20%5Cend%7Bbmatrix%7D%2C%20%5Cquad%20A%20%3D%20%5Cbegin%7Bbmatrix%7D%201%20%26%201%20%5C%5C%201%20%26%202%20%5C%5C%201%20%26%203%20%5Cend%7Bbmatrix%7D>)


می‌خواهیم ![Math](<https://latex.codecogs.com/svg.latex?s>) را پیدا کنیم:



![Math Formula](<https://latex.codecogs.com/svg.latex?s%20%3D%20A%5E%7B-1%7D%20%5Ccdot%20x>)


اما چون ![Math](<https://latex.codecogs.com/svg.latex?A>) مربع نیست، از روش‌های تقریبی مثل **روش کمترین مربعات** یا **ICA** استفاده می‌کنیم.

---

## ✅ خلاصه نهایی

| عنصر | مقدار |
|------|--------|
| سیگنال اولیه | `x = [7, 6, 5]` |
| میانگین | `6` |
| سیگنال بدون میانگین | `[1, 0, -1]` |
| واریانس (جامعه) | `≈ 0.6667` |
| واریانس (نمونه) | `1` |
| انحراف معیار (جامعه) | `≈ 0.816` |
| انحراف معیار (نمونه) | `1` |

---

اگر خواستی این محاسبات را برای یک سیگنال واقعی یا داده‌های EEG واقعی انجام دهم، فقط بگو!