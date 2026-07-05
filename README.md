# Retail Analysis Projects

هذا المشروع عبارة عن حل كامل لتحليل مبيعات البيع بالتجزئة والتنبؤ بها باستخدام بيانات Walmart الأسبوعية. يركز المشروع على فهم سلوك المبيعات، اكتشاف القيم الشاذة، تصميم الميزات، بناء نماذج تنبؤ، ثم تصدير النتائج إلى Power BI.

## نظرة عامة

المشروع يهدف إلى:
- تحليل بيانات المبيعات الأسبوعية لفهم العوامل المؤثرة على الأداء
- اكتشاف الفترات التي تشهد مبيعات مرتفعة أو منخفضة بشكل غير اعتيادي
- بناء ميزات إضافية مثل الإشارات الخاصة بالأعياد ونهاية العام والأحداث المهمة
- تدريب نموذج تنبؤ لمبيعات المستقبل
- تقديم نتائج قابلة للعرض والتحليل عبر Power BI

## ما الذي يقدمه المشروع

- تحليل بيانات retail بشكل عملي وواقعي
- تنظيف وتحضير البيانات قبل النمذجة
- اكتشاف القيم الشاذة وربطها بأسباب محتملة
- استخراج سمات مهمة مثل:
  - Holiday events
  - High sales periods
  - Year-end periods
- مقارنة نماذج تنبؤ مختلفة
- حفظ النموذج النهائي لاستخدامه لاحقًا
- إنشاء ملف تنبؤات جاهز للاستيراده إلى Power BI

## مصدر البيانات

المشروع يستخدم ملف CSV أساسي يحتوي على بيانات أسبوعية لمبيعات Walmart:

- Store
- Date
- Weekly_Sales
- Holiday_Flag
- Temperature
- Fuel_Price
- CPI
- Unemployment

الملف موجود في:
- data/Walmart_Data_Analysis_and_Forcasting.csv

تمت معالجة البيانات وإعدادها لاحقًا في ملفات Pickle داخل:
- data/proccessed/

## هيكل المستودع

```text
retail-analysis-projects/
├── data/
│   ├── Walmart_Data_Analysis_and_Forcasting.csv
│   └── proccessed/
│       ├── retail_clean.pkl
│       ├── retail_after_format.pkl
│       └── data_encoded.pkl
├── model/
│   └── xgb_sales_model.pkl
├── notebooks/
│   ├── inspect.ipynb
│   ├── quality_check_and_basic_feature.ipynb
│   ├── features.ipynb
│   └── pre_modeling.ipynb
├── powerbi/
│   ├── retail_dashboard.pbix
│   └── sales_predictions_xgb.csv
├── src/
│   ├── cleaning.py
│   ├── features.py
│   └── db.py
├── requirements.txt
├── setup.py
└── README.md
```

## المكوّنات الأساسية

### 1) تنظيف البيانات

الملف:
- src/cleaning.py

يوفر وظائف تساعد في:
- تحليل القيم الشاذة
- ربط كل قيمة شاذة بحالة أو سبب محتمل

### 2) هندسة الميزات

الملف:
- src/features.py

يوفر وظائف لتحديد:
- الأسابيع ذات المبيعات المرتفعة
- الأسابيع ذات الإجازات
- أسابيع نهاية السنة
- علامة عامة تشير إلى الأسابيع المهمة

### 3) النمذجة

تم العمل على عدة مراحل نمذجة، من بينها:
- نموذج Ridge Regression كقاعدة أولية
- تحسين التقسيم الزمني للبيانات لتجنب تسريب البيانات المستقبلية
- استخدام XGBoost كالنموذج النهائي الأقوى

النموذج النهائي محفوظ هنا:
- model/xgb_sales_model.pkl

### 4) Power BI

تمت إضافة مخرجات جاهزة للعرض والتحليل في:
- powerbi/retail_dashboard.pbix
- powerbi/sales_predictions_xgb.csv

## المتطلبات

لتشغيل المشروع، تحتاج إلى بيئة Python مع المكتبات التالية:

- pandas
- numpy
- scikit-learn
- xgboost
- matplotlib
- seaborn
- joblib

يمكن تثبيت كل المتطلبات عبر:

```bash
pip install -r requirements.txt
```

## الإعداد والتشغيل

### 1) استنساخ المشروع

```bash
git clone https://github.com/Zainalabdeen-shraf/retail-analysis-projects.git
cd retail-analysis-projects
```

### 2) إنشاء بيئة افتراضية

```bash
python -m venv .venv
```

#### على Windows

```bash
.venv\Scripts\activate
```

#### على macOS / Linux

```bash
source .venv/bin/activate
```

### 3) تثبيت المكتبات

```bash
pip install -r requirements.txt
```

## استخدام المشروع

### استكشاف البيانات باستخدام Jupyter Notebooks

افتح ملفات الـ notebooks التالية بالترتيب:

1. inspect.ipynb
2. quality_check_and_basic_feature.ipynb
3. features.ipynb
4. pre_modeling.ipynb

### أمثلة برمجية سريعة

```python
import pandas as pd
from src.cleaning import analyze_outliers
from src.features import identify_important_weeks

# قراءة البيانات

df = pd.read_csv("data/Walmart_Data_Analysis_and_Forcasting.csv")

# تحليل القيم الشاذة
outliers = analyze_outliers(df, ["Weekly_Sales", "Temperature", "Fuel_Price"])

# استخراج الميزات المهمة
feature_df = identify_important_weeks(df)
```

## النتائج المتوقعة من المشروع

من خلال هذا المشروع يمكنك الحصول على:
- فهم أعمق لعوامل تأثير المبيعات
- رؤى عملية على الأسابيع المهمة
- تنبؤات لأسعار أو مبيعات المستقبل
- لوحة تحكم جاهزة في Power BI

## ملاحظات مهمة

- البيانات الأصلية موجودة في ملف CSV
- توجد نسخ معالجة مسبقًا في مجلد data/proccessed
- ملفات الـ notebooks تحتوي على الخطوات الكاملة للتحليل والنمذجة
- تم اعتماد نهج علمي في النمذجة مع مراعاة التسلسل الزمني للبيانات

## الخلاصة

هذا المشروع يمثل مثالًا عمليًا على pipeline كامل في تحليل البيانات والتنبؤ بالبيع بالتجزئة، من جمع البيانات إلى النمذجة إلى العرض النهائي.

إذا كنت تريد، يمكنني أيضًا تجهيز نسخة أكثر احترافية من هذا الملف بصيغة README احترافية جدًا تناسب GitHub، أو إضافة قسم “How to contribute” و “License”.
