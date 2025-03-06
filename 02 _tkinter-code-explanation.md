# شرح مفصل لأكواد بايثون لواجهات Tkinter

## الكود الأول: تطبيق Hello World مع واجهة متقدمة

هذا الكود يستخدم البرمجة كائنية التوجه (OOP) لإنشاء تطبيق رسومي يسمح للمستخدم بإدخال اسمه وعرض رسالة ترحيب مخصصة.

### استيراد المكتبات

```python
import tkinter as tk
from tkinter import ttk
```

- `import tkinter as tk`: يستورد مكتبة tkinter الأساسية ويعطيها اسم مختصر `tk` للاستخدام اللاحق
- `from tkinter import ttk`: يستورد حزمة ttk (themed Tkinter) التي توفر عناصر واجهة محسنة ذات مظهر أكثر حداثة

### تعريف فئة HelloView

```python
class HelloView(tk.Frame):
```

- هنا يتم إنشاء فئة (class) جديدة تسمى `HelloView` ترث من `tk.Frame`
- `tk.Frame` هو حاوية أساسية في Tkinter تستخدم لتجميع عناصر الواجهة

### دالة البناء للفئة

```python
def __init__(self, parent, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
```

- `__init__`: هي دالة البناء (constructor) التي تُستدعى عند إنشاء كائن جديد من هذه الفئة
- `self`: يشير إلى الكائن نفسه
- `parent`: العنصر الأب الذي سيحتوي هذا الإطار
- `*args, **kwargs`: تسمح بتمرير معاملات إضافية غير محددة مسبقًا
- `super().__init__(parent, *args, **kwargs)`: يستدعي دالة البناء للفئة الأب (`tk.Frame`) لتهيئة الإطار بشكل صحيح

### تعريف متغيرات Tkinter

```python
self.name = tk.StringVar()
self.hello_string = tk.StringVar(value="Hello World")
```

- `tk.StringVar()`: يُنشئ متغير نصي خاص بـ Tkinter يمكن ربطه بعناصر الواجهة
- `self.name`: متغير لتخزين الاسم الذي سيدخله المستخدم
- `self.hello_string`: متغير لتخزين رسالة الترحيب، تم تعيين قيمته الأولية بـ "Hello World"

### إنشاء مكونات الواجهة

```python
name_label = tk.Label(self, text="Name:")
name_entry = tk.Entry(self, textvariable=self.name)
ch_button = ttk.Button(self, text="Change", command=self.on_change)
hello_label = tk.Label(
    self, textvariable=self.hello_string, 
    font=("TkDefaultFont", 64), wraplength=600
)
```

- `tk.Label(self, text="Name:")`: إنشاء علامة نصية تعرض "Name:"
- `tk.Entry(self, textvariable=self.name)`: إنشاء حقل إدخال نصي مرتبط بمتغير `self.name`
- `ttk.Button(self, text="Change", command=self.on_change)`: إنشاء زر يعرض "Change" وعند النقر عليه ينفذ الدالة `self.on_change`
- `tk.Label(...)`: إنشاء علامة نصية كبيرة لعرض رسالة الترحيب
  - `textvariable=self.hello_string`: ربط العلامة بمتغير `self.hello_string`
  - `font=("TkDefaultFont", 64)`: تحديد خط العلامة وحجمه (64)
  - `wraplength=600`: تحديد عرض العلامة، بحيث ينتقل النص إلى سطر جديد إذا تجاوز 600 بكسل

### ترتيب العناصر باستخدام Grid

```python
name_label.grid(row=0, column=0, sticky=tk.W)
name_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
ch_button.grid(row=0, column=2, sticky=tk.E)
hello_label.grid(row=1, column=0, columnspan=3)
```

- `grid`: طريقة لتنظيم العناصر في شبكة من الصفوف والأعمدة
- `row=0, column=0`: تحديد موقع العنصر في الصف والعمود
- `sticky=tk.W`: يجعل العنصر "يلتصق" بالجانب الغربي (اليسار) من الخلية
- `sticky=(tk.W, tk.E)`: يجعل العنصر يمتد ليملأ الخلية من اليسار إلى اليمين
- `columnspan=3`: يجعل العنصر يمتد عبر 3 أعمدة

### تكوين الأعمدة

```python
self.columnconfigure(1, weight=1)
```

- يعطي العمود رقم 1 (الذي يحتوي على حقل الإدخال) وزنًا بقيمة 1، مما يجعله يتمدد عند تغيير حجم النافذة

### دالة معالجة تغيير النص

```python
def on_change(self):
    if self.name.get().strip():
        self.hello_string.set(f"Hello {self.name.get()}")
    else:
        self.hello_string.set("Hello World")
```

- تتحقق مما إذا كان المستخدم قد أدخل اسمًا (غير فارغ بعد إزالة المسافات)
- إذا كان هناك اسم، تقوم بتعيين متغير `hello_string` إلى "Hello" متبوعًا بالاسم
- إذا كان الاسم فارغًا، تعيد تعيين النص إلى "Hello World"
- باستخدام `.get()` نحصل على قيمة متغير Tkinter كنص عادي
- باستخدام `.set()` نقوم بتعيين قيمة جديدة لمتغير Tkinter

### تعريف فئة التطبيق الرئيسي

```python
class MyApplication(tk.Tk):
    """ تطبيق Tkinter لعرض رسالة ترحيب مخصصة """
```

- إنشاء فئة تمثل التطبيق بأكمله، ترث من `tk.Tk` (النافذة الرئيسية لـ Tkinter)
- يتضمن تعليقًا توثيقيًا (docstring) يشرح الغرض من هذه الفئة

### دالة البناء للتطبيق

```python
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.title("Hello Tkinter")
    self.geometry("800x600")
    self.resizable(width=False, height=False)
```

- `super().__init__(*args, **kwargs)`: يستدعي دالة البناء للفئة الأب (`tk.Tk`)
- `self.title("Hello Tkinter")`: يعين عنوان النافذة
- `self.geometry("800x600")`: يحدد حجم النافذة (عرض 800 بكسل وارتفاع 600 بكسل)
- `self.resizable(width=False, height=False)`: يمنع المستخدم من تغيير حجم النافذة

### إضافة الواجهة للتطبيق

```python
self.view = HelloView(self)
self.view.grid(sticky=(tk.W, tk.E, tk.N, tk.S))
self.columnconfigure(0, weight=1)
```

- `self.view = HelloView(self)`: ينشئ كائنًا من فئة `HelloView` ويمرر النافذة الرئيسية كعنصر أب
- `self.view.grid(sticky=(tk.W, tk.E, tk.N, tk.S))`: يضع الإطار في النافذة الرئيسية ويجعله يمتد في جميع الاتجاهات
- `self.columnconfigure(0, weight=1)`: يجعل العمود 0 (الوحيد) يتمدد مع تغيير حجم النافذة

### نقطة بداية البرنامج

```python
if __name__ == "__main__":
    app = MyApplication()
    app.mainloop()
```

- `if __name__ == "__main__"`: يتحقق مما إذا كان هذا الملف يتم تشغيله مباشرة وليس استيراده
- `app = MyApplication()`: ينشئ كائنًا من فئة `MyApplication` (النافذة الرئيسية)
- `app.mainloop()`: يبدأ حلقة الأحداث الرئيسية للتطبيق، وهي تستمر في الاستماع للأحداث (مثل النقر والكتابة) حتى يتم إغلاق التطبيق

## الكود الثاني: تطبيق Hello World بسيط

هذا الكود هو نسخة مبسطة جدًا من تطبيق Hello World باستخدام Tkinter.

### استيراد المكتبات

```python
from tkinter import *
from tkinter.ttk import *
```

- `from tkinter import *`: يستورد جميع الدوال والفئات من مكتبة tkinter مباشرة إلى نطاق الكود الحالي
- `from tkinter.ttk import *`: يستورد جميع العناصر من مكتبة ttk

> ملاحظة: استخدام `import *` ليس ممارسة مفضلة في البرمجة لأنه قد يؤدي إلى تعارضات في الأسماء ويجعل من الصعب تتبع مصدر الدوال والفئات المستخدمة.

### إنشاء النافذة الرئيسية

```python
root = Tk()
root.title("Hello World")
```

- `root = Tk()`: ينشئ نافذة رئيسية جديدة
- `root.title("Hello World")`: يعيّن عنوان النافذة إلى "Hello World"

### إضافة علامة نصية

```python
label = Label(root, text="Hello World")
label.pack()
```

- `label = Label(root, text="Hello World")`: ينشئ علامة نصية تعرض "Hello World"
- `label.pack()`: يضع العلامة في النافذة باستخدام مدير التخطيط `pack`، الذي يقوم تلقائيًا بتوسيط العنصر

### بدء حلقة الأحداث

```python
root.mainloop()
```

- `root.mainloop()`: يبدأ حلقة الأحداث الرئيسية للتطبيق، والتي تستمر حتى يتم إغلاق النافذة

## مقارنة بين الكودين

1. **نهج البرمجة**:
   - الكود الأول يستخدم البرمجة كائنية التوجه (OOP) بتعريف فئات مخصصة
   - الكود الثاني يستخدم نهجًا إجرائيًا بسيطًا

2. **استيراد المكتبات**:
   - الكود الأول يستخدم استيرادًا محددًا مع أسماء مستعارة (`import tkinter as tk`)
   - الكود الثاني يستخدم استيراد كامل (`from tkinter import *`)

3. **التعقيد**:
   - الكود الأول معقد أكثر لكنه أكثر قابلية للتوسع والصيانة
   - الكود الثاني بسيط وسهل الفهم لكنه غير قابل للتوسع بسهولة

4. **الوظائف**:
   - الكود الأول يوفر واجهة تفاعلية مع إدخال وزر وتغيير ديناميكي للنص
   - الكود الثاني يعرض فقط علامة نصية ثابتة

5. **مديرو التخطيط**:
   - الكود الأول يستخدم `grid` الذي يوفر تحكمًا دقيقًا في موضع العناصر
   - الكود الثاني يستخدم `pack` الذي يقوم تلقائيًا بترتيب العناصر
