# تنظيم وترتيب حقول النموذج في Tkinter

## اختيار طريقة تنظيم الحقول في Tkinter

عند إنشاء نموذج إدخال بيانات باستخدام Tkinter، من المهم تنظيم الحقول بطريقة منطقية وسهلة الاستخدام. يمكننا استخدام عدة طرق لتمييز مجموعات الحقول بصريًا في الواجهة الرسومية:

### خيارات تنظيم مجموعات الحقول

* **ttk.LabelFrame**: 
  * إطار يحتوي على عنوان ونص توضيحي
  * يعتبر الخيار الأنسب لتجميع الحقول المرتبطة
  * يضيف حدودًا واضحة وعنوانًا لكل مجموعة

* **ttk.Notebook**: 
  * عنصر واجهة يحتوي على علامات تبويب للانتقال بين الصفحات
  * غير مناسب إذا كنا نريد نموذج إدخال واحد فقط
  * مفيد للنماذج الكبيرة التي تحتاج إلى تقسيم على صفحات متعددة

* **Tkinter.PanedWindow**: 
  * يسمح بترتيب الحقول أفقيًا أو عموديًا مع إمكانية إعادة ضبط الحجم
  * غير ضروري للنماذج البسيطة
  * مفيد للواجهات المعقدة التي تحتاج إلى تقسيمات قابلة للتعديل

### الاختيار الأمثل

**ttk.LabelFrame** هو الخيار الأفضل لمعظم نماذج الإدخال لأنه:
* يسمح بتنظيم الحقول داخل أقسام واضحة
* يجعل واجهة المستخدم أكثر وضوحًا
* يسهّل على المستخدم فهم العلاقة بين الحقول المختلفة

## تنسيق الحقول داخل النموذج

بعد تصنيف الحقول إلى مجموعات، نحتاج إلى ترتيبها داخل النموذج بطريقة منظمة وسهلة الاستخدام. توفر Tkinter ثلاث طرق أساسية لترتيب العناصر داخل النافذة.

### خيارات ترتيب الحقول في Tkinter

| الطريقة | الوصف | المزايا | العيوب |
|---------|-------|---------|---------|
| **grid** | نظام الشبكة، يسمح بوضع العناصر في صفوف وأعمدة | دقيق، مرن، سهل التخطيط | يحتاج إلى تخطيط مسبق |
| **pack** | يضع العناصر بشكل متتابع أفقيًا أو عموديًا | بسيط، جيد للتخطيطات البسيطة | صعب للتخطيطات المعقدة |
| **place** | يحدد موقع العناصر باستخدام الإحداثيات المطلقة | دقة عالية جدًا في التموضع | صعب الصيانة، غير متجاوب |

### الاختيار الأنسب

**grid** هو الأفضل لمعظم نماذج الإدخال للأسباب التالية:
* يسمح بترتيب الحقول في صفوف وأعمدة محددة
* يساعد على إبقاء الحقول مرتبة ضمن المجموعات
* يعطي مرونة في تنظيم العناصر المختلفة
* يسهل محاذاة العناصر (مثل وضع التسميات في عمود والحقول في عمود آخر)

## مثال عملي على ترتيب الحقول

فيما يلي مثال يوضح كيفية ترتيب الحقول داخل النافذة باستخدام `grid` و `LabelFrame`:

```python
import tkinter as tk
from tkinter import ttk

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("نموذج إدخال البيانات")

# إنشاء إطار لمعلومات السجل
record_frame = ttk.LabelFrame(root, text="معلومات السجل")
record_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# إنشاء الحقول داخل إطار "معلومات السجل"
ttk.Label(record_frame, text="التاريخ:").grid(row=0, column=0, padx=5, pady=5)
date_entry = ttk.Entry(record_frame)
date_entry.grid(row=0, column=1, padx=5, pady=5)

# إضافة حقل المختبر
ttk.Label(record_frame, text="المختبر:").grid(row=1, column=0, padx=5, pady=5)
lab_combobox = ttk.Combobox(record_frame)
lab_combobox.grid(row=1, column=1, padx=5, pady=5)

# تكرار نفس الفكرة للمجموعات الأخرى...

# تشغيل التطبيق
root.mainloop()
```

### شرح الكود

1. **إنشاء النافذة الرئيسية**:
   ```python
   root = tk.Tk()
   root.title("نموذج إدخال البيانات")
   ```
   * ينشئ نافذة جديدة
   * يضبط عنوان النافذة

2. **إنشاء LabelFrame لتجميع الحقول المرتبطة**:
   ```python
   record_frame = ttk.LabelFrame(root, text="معلومات السجل")
   record_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
   ```
   * ينشئ إطارًا مسمى بعنوان "معلومات السجل"
   * يضعه في الصف 0، العمود 0 من النافذة الرئيسية
   * يضيف هوامش (padding) بقيمة 10 بكسل حول الإطار
   * `sticky="ew"` يجعل الإطار يمتد أفقيًا (شرق-غرب)

3. **إضافة التسميات والحقول داخل الإطار**:
   ```python
   ttk.Label(record_frame, text="التاريخ:").grid(row=0, column=0, padx=5, pady=5)
   date_entry = ttk.Entry(record_frame)
   date_entry.grid(row=0, column=1, padx=5, pady=5)
   ```
   * ينشئ تسمية (Label) وحقل إدخال (Entry) داخل الإطار
   * يضع التسمية في العمود 0 والحقل في العمود 1 من نفس الصف
   * يضيف هوامش صغيرة حول كل عنصر

## مثال متكامل لنموذج بيانات

فيما يلي مثال أكثر تفصيلاً لنموذج بيانات كامل باستخدام مجموعات متعددة:

```python
import tkinter as tk
from tkinter import ttk

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("نموذج تسجيل العينات المختبرية")
root.geometry("650x500")  # تحديد حجم النافذة

# إنشاء إطار لمعلومات السجل
record_frame = ttk.LabelFrame(root, text="معلومات السجل")
record_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

# إضافة حقول معلومات السجل
ttk.Label(record_frame, text="رقم العينة:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
sample_id = ttk.Entry(record_frame)
sample_id.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(record_frame, text="التاريخ:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
date_entry = ttk.Entry(record_frame)
date_entry.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

ttk.Label(record_frame, text="المختبر:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
lab_combobox = ttk.Combobox(record_frame, values=["مختبر الكيمياء", "مختبر الأحياء", "مختبر الفيزياء"])
lab_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(record_frame, text="الفني المسؤول:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
technician_entry = ttk.Entry(record_frame)
technician_entry.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

# ضبط أوزان الأعمدة
for i in range(4):
    record_frame.columnconfigure(i, weight=1)

# إنشاء إطار لمعلومات العينة
sample_frame = ttk.LabelFrame(root, text="معلومات العينة")
sample_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# إضافة حقول معلومات العينة
ttk.Label(sample_frame, text="نوع العينة:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
sample_type = ttk.Combobox(sample_frame, values=["دم", "بول", "أنسجة", "أخرى"])
sample_type.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(sample_frame, text="مصدر العينة:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
source_entry = ttk.Entry(sample_frame)
source_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(sample_frame, text="حالة العينة:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
status_combobox = ttk.Combobox(sample_frame, values=["جيدة", "تالفة", "غير مكتملة"])
status_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

# ضبط أوزان الأعمدة
for i in range(2):
    sample_frame.columnconfigure(i, weight=1)

# إنشاء إطار للفحوصات المطلوبة
tests_frame = ttk.LabelFrame(root, text="الفحوصات المطلوبة")
tests_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# إضافة خيارات الفحوصات
test1_var = tk.BooleanVar()
test1 = ttk.Checkbutton(tests_frame, text="فحص الجلوكوز", variable=test1_var)
test1.grid(row=0, column=0, padx=5, pady=5, sticky="w")

test2_var = tk.BooleanVar()
test2 = ttk.Checkbutton(tests_frame, text="فحص الكوليسترول", variable=test2_var)
test2.grid(row=1, column=0, padx=5, pady=5, sticky="w")

test3_var = tk.BooleanVar()
test3 = ttk.Checkbutton(tests_frame, text="فحص وظائف الكبد", variable=test3_var)
test3.grid(row=2, column=0, padx=5, pady=5, sticky="w")

test4_var = tk.BooleanVar()
test4 = ttk.Checkbutton(tests_frame, text="فحص وظائف الكلى", variable=test4_var)
test4.grid(row=3, column=0, padx=5, pady=5, sticky="w")

# إنشاء إطار للملاحظات
notes_frame = ttk.LabelFrame(root, text="ملاحظات إضافية")
notes_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# إضافة مربع نص للملاحظات
notes_text = tk.Text(notes_frame, height=5, width=50)
notes_text.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

# إضافة شريط تمرير للملاحظات
scrollbar = ttk.Scrollbar(notes_frame, orient="vertical", command=notes_text.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
notes_text.configure(yscrollcommand=scrollbar.set)

# ضبط أوزان الأعمدة والصفوف في الإطار الرئيسي
notes_frame.columnconfigure(0, weight=1)
notes_frame.rowconfigure(0, weight=1)

# إضافة أزرار التحكم
control_frame = ttk.Frame(root)
control_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

save_button = ttk.Button(control_frame, text="حفظ البيانات")
save_button.grid(row=0, column=0, padx=5, pady=5)

clear_button = ttk.Button(control_frame, text="مسح الحقول")
clear_button.grid(row=0, column=1, padx=5, pady=5)

exit_button = ttk.Button(control_frame, text="إغلاق", command=root.destroy)
exit_button.grid(row=0, column=2, padx=5, pady=5)

# ضبط موضع الأزرار في المنتصف
control_frame.columnconfigure(0, weight=1)
control_frame.columnconfigure(1, weight=1)
control_frame.columnconfigure(2, weight=1)

# ضبط أوزان الصفوف والأعمدة في النافذة الرئيسية
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# تشغيل التطبيق
root.mainloop()
```

## ملخص واستنتاجات

عند تصميم نموذج إدخال بيانات باستخدام Tkinter، يمكننا اتباع الخطوات التالية:

1. **تحديد وتصنيف الحقول المطلوبة**:
   * تجميع الحقول المرتبطة معًا
   * تقسيم النموذج إلى أقسام منطقية

2. **اختيار طريقة تنظيم الحقول**:
   * استخدام `ttk.LabelFrame` لتجميع الحقول المرتبطة
   * تخصيص عنوان واضح لكل مجموعة

3. **اختيار طريقة تنسيق العناصر**:
   * استخدام `grid` للحصول على تحكم دقيق في تموضع العناصر
   * تنظيم التسميات والحقول في صفوف وأعمدة متناسقة

4. **تحسين تجربة المستخدم**:
   * إضافة هوامش (`padx` و `pady`) لجعل الواجهة أكثر جاذبية
   * استخدام خاصية `sticky` لمحاذاة العناصر بشكل صحيح
   * تعيين أوزان الصفوف والأعمدة (`weight`) للتحكم في كيفية توسيع العناصر

5. **إضافة عناصر التحكم**:
   * أزرار لحفظ البيانات أو مسح الحقول أو إغلاق النموذج
   * وضع العناصر في أماكن منطقية وسهلة الوصول

باتباع هذه الإرشادات، يمكننا إنشاء نماذج إدخال بيانات جذابة وسهلة الاستخدام باستخدام Tkinter.
