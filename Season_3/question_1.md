برای حل سوال ۲، باید از داده‌های موجود در جدول و فرمول SNR استفاده کنیم. هدف محاسبه مقدار **SNR** برای سیگنال‌های نویزدار با استفاده از دو روش مختلف — **Median Filter** و **Ensemble Averaging** — است.

### **داده‌ها:**
- **سیگنال اصلی (Original):** `[3, 9, 5, 7, 6]`
- **سیگنال‌های نویزدار (Noisy signals):**
  - Noisy signal 1: `[3.2, 8.1, 4.7, 7.4, 6.1]`
  - Noisy signal 2: `[2.9, 9.1, 5.1, 6.4, 5.8]`
  - Noisy signal 3: `[3.1, 8.7, 5.3, 7.1, 6.2]`
  - Noisy signal 4: `[2.7, 8.8, 4.9, 7.2, 5.8]`

### **فرمول محاسبه SNR:**


![Math Formula](<https://latex.codecogs.com/svg.latex?%5Ctext%7BSNR%7D%20%3D%2010%20%5Clog_%7B10%7D%20%5Cleft%28%20%5Cfrac%7BE_%7B%5Ctext%7Bsignal%7D%7D%7D%7BE_%7B%5Ctext%7Bnoise%7D%7D%7D%20%5Cright%29>)

که:
- ![Math](<https://latex.codecogs.com/svg.latex?E_%7B%5Ctext%7Bsignal%7D%7D>): انرژی سیگنال اصلی
- ![Math](<https://latex.codecogs.com/svg.latex?E_%7B%5Ctext%7Bnoise%7D%7D>): انرژی نویز

#### **انرژی سیگنال (![Math](<https://latex.codecogs.com/svg.latex?E_%7B%5Ctext%7Bsignal%7D%7D>)):**
انرژی سیگنال اصلی به صورت زیر محاسبه می‌شود:


![Math Formula](<https://latex.codecogs.com/svg.latex?E_%7B%5Ctext%7Bsignal%7D%7D%20%3D%20%5Csum_%7Bn%3D0%7D%5E%7BN-1%7D%20x%5Bn%5D%5E2>)

که ![Math](<https://latex.codecogs.com/svg.latex?x%5Bn%5D>) سیگنال اصلی است و ![Math](<https://latex.codecogs.com/svg.latex?N>) طول سیگنال است.

#### **انرژی نویز (![Math](<https://latex.codecogs.com/svg.latex?E_%7B%5Ctext%7Bnoise%7D%7D>)):**
انرژی نویز برای هر روش حذف نویز (Median Filter و Ensemble Averaging) به صورت زیر محاسبه می‌شود:


![Math Formula](<https://latex.codecogs.com/svg.latex?E_%7B%5Ctext%7Bnoise%7D%7D%20%3D%20%5Csum_%7Bn%3D0%7D%5E%7BN-1%7D%20e%5Bn%5D%5E2>)

که ![Math](<https://latex.codecogs.com/svg.latex?e%5Bn%5D>) نویز است و ![Math](<https://latex.codecogs.com/svg.latex?e%5Bn%5D%20%3D%20%5Ctext%7BNoisy%20signal%7D%5Bn%5D%20-%20%5Ctext%7BFiltered%20signal%7D%5Bn%5D>).

---

### **مرحله 1: محاسبه انرژی سیگنال اصلی (![Math](<https://latex.codecogs.com/svg.latex?E_%7B%5Ctext%7Bsignal%7D%7D>))**

سیگنال اصلی: ![Math](<https://latex.codecogs.com/svg.latex?x%5Bn%5D%20%3D%20%5B3%2C%209%2C%205%2C%207%2C%206%5D>)



![Math Formula](<https://latex.codecogs.com/svg.latex?E_%7B%5Ctext%7Bsignal%7D%7D%20%3D%20%5Csum_%7Bn%3D0%7D%5E%7B4%7D%20x%5Bn%5D%5E2%20%3D%203%5E2%20%2B%209%5E2%20%2B%205%5E2%20%2B%207%5E2%20%2B%206%5E2>)



![Math Formula](<https://latex.codecogs.com/svg.latex?E_%7B%5Ctext%7Bsignal%7D%7D%20%3D%209%20%2B%2081%20%2B%2025%20%2B%2049%20%2B%2036%20%3D%20200>)


---

### **مرحله 2: محاسبه انرژی نویز برای Median Filter**

#### **محاسبه میانه (Median) سیگنال‌های نویزدار:**
برای هر نمونه، میانه مقادیر متناظر در سیگنال‌های نویزدار را محاسبه می‌کنیم:

- نمونه 0: `[3.2, 2.9, 3.1, 2.7]` → میانه = `3`
- نمونه 1: `[8.1, 9.1, 8.7, 8.8]` → میانه = `8.7`
- نمونه 2: `[4.7, 5.1, 5.3, 4.9]` → میانه = `5`
- نمونه 3: `[7.4, 6.4, 7.1, 7.2]` → میانه = `7.1`
- نمونه 4: `[6.1, 5.8, 6.2, 5.8]` → میانه = `5.8`

سیگنال پس از Median Filter: ![Math](<https://latex.codecogs.com/svg.latex?%5Ctext%7BFiltered%20signal%7D%20%3D%20%5B3%2C%208.7%2C%205%2C%207.1%2C%205.8%5D>)

#### **محاسبه نویز برای Median Filter:**


![Math Formula](<https://latex.codecogs.com/svg.latex?e%5Bn%5D%20%3D%20%5Ctext%7BNoisy%20signal%7D%5Bn%5D%20-%20%5Ctext%7BFiltered%20signal%7D%5Bn%5D>)


- نمونه 0: ![Math](<https://latex.codecogs.com/svg.latex?e%5B0%5D%20%3D%203.2%20-%203%20%3D%200.2>)
- نمونه 1: ![Math](<https://latex.codecogs.com/svg.latex?e%5B1%5D%20%3D%208.1%20-%208.7%20%3D%20-0.6>)
- نمونه 2: ![Math](<https://latex.codecogs.com/svg.latex?e%5B2%5D%20%3D%204.7%20-%205%20%3D%20-0.3>)
- نمونه 3: ![Math](<https://latex.codecogs.com/svg.latex?e%5B3%5D%20%3D%207.4%20-%207.1%20%3D%200.3>)
- نمونه 4: ![Math](<https://latex.codecogs.com/svg.latex?e%5B4%5D%20%3D%206.1%20-%205.8%20%3D%200.3>)

نویز: ![Math](<https://latex.codecogs.com/svg.latex?e%5Bn%5D%20%3D%20%5B0.2%2C%20-0.6%2C%20-0.3%2C%200.3%2C%200.3%5D>)

#### **محاسبه انرژی نویز برای Median Filter:**


![Math Formula](<https://latex.codecogs.com/svg.latex?E_%7B%5Ctext%7Bnoise%7D%7D%20%3D%20%5Csum_%7Bn%3D0%7D%5E%7B4%7D%20e%5Bn%5D%5E2%20%3D%200.2%5E2%20%2B%20%28-0.6%29%5E2%20%2B%20%28-0.3%29%5E2%20%2B%200.3%5E2%20%2B%200.3%5E2>)



![Math Formula](<https://latex.codecogs.com/svg.latex?E_%7B%5Ctext%7Bnoise%7D%7D%20%3D%200.04%20%2B%200.36%20%2B%200.09%20%2B%200.09%20%2B%200.09%20%3D%200.67>)


#### **محاسبه SNR برای Median Filter:**


![Math Formula](<https://latex.codecogs.com/svg.latex?%5Ctext%7BSNR%7D_%7B%5Ctext%7BMedian%7D%7D%20%3D%2010%20%5Clog_%7B10%7D%20%5Cleft%28%20%5Cfrac%7BE_%7B%5Ctext%7Bsignal%7D%7D%7D%7BE_%7B%5Ctext%7Bnoise%7D%7D%7D%20%5Cright%29%20%3D%2010%20%5Clog_%7B10%7D%20%5Cleft%28%20%5Cfrac%7B200%7D%7B0.67%7D%20%5Cright%29>)



![Math Formula](<https://latex.codecogs.com/svg.latex?%5Ctext%7BSNR%7D_%7B%5Ctext%7BMedian%7D%7D%20%3D%2010%20%5Clog_%7B10%7D%20%28298.5075%29%20%5Capprox%2010%20%5Ctimes%201.4749%20%5Capprox%2014.75%20%5C%2C%20%5Ctext%7BdB%7D>)


---

### **مرحله 3: محاسبه انرژی نویز برای Ensemble Averaging**

#### **محاسبه میانگین تجمعی (Ensemble Averaging):**
برای هر نمونه، میانگین مقادیر متناظر در سیگنال‌های نویزدار را محاسبه می‌کنیم:

- نمونه 0: ![Math](<https://latex.codecogs.com/svg.latex?%5Cfrac%7B3.2%20%2B%202.9%20%2B%203.1%20%2B%202.7%7D%7B4%7D%20%3D%20%5Cfrac%7B11.9%7D%7B4%7D%20%3D%202.975>)
- نمونه 1: ![Math](<https://latex.codecogs.com/svg.latex?%5Cfrac%7B8.1%20%2B%209.1%20%2B%208.7%20%2B%208.8%7D%7B4%7D%20%3D%20%5Cfrac%7B34.7%7D%7B4%7D%20%3D%208.675>)
- نمونه 2: ![Math](<https://latex.codecogs.com/svg.latex?%5Cfrac%7B4.7%20%2B%205.1%20%2B%205.3%20%2B%204.9%7D%7B4%7D%20%3D%20%5Cfrac%7B20%7D%7B4%7D%20%3D%205>)
- نمونه 3: ![Math](<https://latex.codecogs.com/svg.latex?%5Cfrac%7B7.4%20%2B%206.4%20%2B%207.1%20%2B%207.2%7D%7B4%7D%20%3D%20%5Cfrac%7B28.1%7D%7B4%7D%20%3D%207.025>)
- نمونه 4: ![Math](<https://latex.codecogs.com/svg.latex?%5Cfrac%7B6.1%20%2B%205.8%20%2B%206.2%20%2B%205.8%7D%7B4%7D%20%3D%20%5Cfrac%7B23.9%7D%7B4%7D%20%3D%205.975>)

سیگنال پس از Ensemble Averaging: ![Math](<https://latex.codecogs.com/svg.latex?%5Ctext%7BFiltered%20signal%7D%20%3D%20%5B2.975%2C%208.675%2C%205%2C%207.025%2C%205.975%5D>)

#### **محاسبه نویز برای Ensemble Averaging:**


![Math Formula](<https://latex.codecogs.com/svg.latex?e%5Bn%5D%20%3D%20%5Ctext%7BNoisy%20signal%7D%5Bn%5D%20-%20%5Ctext%7BFiltered%20signal%7D%5Bn%5D>)


- نمونه 0: ![Math](<https://latex.codecogs.com/svg.latex?e%5B0%5D%20%3D%203.2%20-%202.975%20%3D%200.225>)
- نمونه 1: ![Math](<https://latex.codecogs.com/svg.latex?e%5B1%5D%20%3D%208.1%20-%208.675%20%3D%20-0.575>)
- نمونه 2: ![Math](<https://latex.codecogs.com/svg.latex?e%5B2%5D%20%3D%204.7%20-%205%20%3D%20-0.3>)
- نمونه 3: ![Math](<https://latex.codecogs.com/svg.latex?e%5B3%5D%20%3D%207.4%20-%207.025%20%3D%200.375>)
- نمونه 4: ![Math](<https://latex.codecogs.com/svg.latex?e%5B4%5D%20%3D%206.1%20-%205.975%20%3D%200.125>)

نویز: ![Math](<https://latex.codecogs.com/svg.latex?e%5Bn%5D%20%3D%20%5B0.225%2C%20-0.575%2C%20-0.3%2C%200.375%2C%200.125%5D>)

#### **محاسبه انرژی نویز برای Ensemble Averaging:**


![Math Formula](<https://latex.codecogs.com/svg.latex?E_%7B%5Ctext%7Bnoise%7D%7D%20%3D%20%5Csum_%7Bn%3D0%7D%5E%7B4%7D%20e%5Bn%5D%5E2%20%3D%200.225%5E2%20%2B%20%28-0.575%29%5E2%20%2B%20%28-0.3%29%5E2%20%2B%200.375%5E2%20%2B%200.125%5E2>)



![Math Formula](<https://latex.codecogs.com/svg.latex?E_%7B%5Ctext%7Bnoise%7D%7D%20%3D%200.050625%20%2B%200.330625%20%2B%200.09%20%2B%200.140625%20%2B%200.015625%20%3D%200.6275>)


#### **محاسبه SNR برای Ensemble Averaging:**


![Math Formula](<https://latex.codecogs.com/svg.latex?%5Ctext%7BSNR%7D_%7B%5Ctext%7BEnsemble%7D%7D%20%3D%2010%20%5Clog_%7B10%7D%20%5Cleft%28%20%5Cfrac%7BE_%7B%5Ctext%7Bsignal%7D%7D%7D%7BE_%7B%5Ctext%7Bnoise%7D%7D%7D%20%5Cright%29%20%3D%2010%20%5Clog_%7B10%7D%20%5Cleft%28%20%5Cfrac%7B200%7D%7B0.6275%7D%20%5Cright%29>)



![Math Formula](<https://latex.codecogs.com/svg.latex?%5Ctext%7BSNR%7D_%7B%5Ctext%7BEnsemble%7D%7D%20%3D%2010%20%5Clog_%7B10%7D%20%28318.75%29%20%5Capprox%2010%20%5Ctimes%201.5033%20%5Capprox%2015.03%20%5C%2C%20%5Ctext%7BdB%7D>)


---

### **نتیجه نهایی:**
- **SNR برای Median Filter:** ![Math](<https://latex.codecogs.com/svg.latex?%5Cboxed%7B14.75%20%5C%2C%20%5Ctext%7BdB%7D%7D>)
- **SNR برای Ensemble Averaging:** ![Math](<https://latex.codecogs.com/svg.latex?%5Cboxed%7B15.03%20%5C%2C%20%5Ctext%7BdB%7D%7D>)