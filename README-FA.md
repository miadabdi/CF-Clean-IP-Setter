# CF-Clean-IP-Setter

این اسکریپت اتوماتیک ایپی های پابلیک کلودفلر و لیست لوکال ورودی رو تست میکنه و روی ساب دامین شما در کلودفلر ست میکنه.
قابلیت بدست اوردن ایپی ها و تست اون ها رو داره تا فایل ریزالت بسازه. و یا اگر نیازی به اسکن ندارین این اسکریپت میتونه فقط به عنوان ست کننده عمل کنه که لیست ایپی هاتون رو بهش بدین و اون هارو روی دامنه ست کنه.

** بخش اسکنر از اسکنر مرتضی باشسیز استفاده میکنه که تنها Vmess+WS+TLS رو ساپورت میکنه **

## نصب

مخزن رو کلون کنید:

```bash
git clone https://github.com/miadabdi/CF-Clean-IP-Setter.git && cd CF-Clean-IP-Setter
```

مخزن اسکنر رو کلون کنید و برای اجرا اماده کنید:

```bash
git clone https://github.com/MortezaBashsiz/CFScanner.git && chmod +x CFScanner/bin/*
```

همچنین خود اسکنر نیاز به دیپندنسی هایی داره که میتونید تو داک خودش بخونید و نصب کنید: docs [here](https://github.com/MortezaBashsiz/CFScanner/tree/main/bash#requirements).

دیپندنسی های پروژه رو نصب کنید:

```bash
pip install -r ./requirements.txt
```

### پیکربندی

قبل از ران کردن اسکریپت شما باید فایل کانفیگ رو بسازید, فایل `config.json.example` رو به فایلی با هر اسمی مثل `config.json` کپی کنید و کامنت هارو حذف کتید.

```bash
cp config.json.example config.json
```

مقادیر در کانفیگ ها به شرح زیر هستن:

- **operator** (string) : آیپی ها برای چ اپراتوری بدست اورده شوند. وقتی یه لیست قایل ایپی به اسکریپت بدین این آپشن هیچ فیلتری روش انجام نمیده چون لیست ورودی ایپی نمایانگر این نیست که ایپی برای چ اپراتوری هست, ولی برای ایپی های پابلیک تاثیر داره و تنها ایپی های مختص اپراتور مشخص شده تست میشن.
- **use_provided_result** (boolean) : مشخص میکنه که ایا شما میخواین با ریزالت فایل خودتون ایپی هارو ست کنین یا اسکریپت باید ایپی ها رو بدست بیاره و تست کنه. فایل ریزالت مطابق با خروجی نسخه بش اسکنر باشسیز هست. [CF Scanner](https://github.com/MortezaBashsiz/CFScanner).
- **last_result_path** (string) : مسیر فایل ریزالت خودتون در این فیلد وارد میشه.
- **include_list_ips** (boolean) : مشخص میکنه که ایا اسکریپت باید از مخزن وحید ایپی بدست بیاره [this repo](https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/list.json)
- **include_list_domains** (boolean) : مشخص میکنه که ایا اسکریپت باید از مخزن وحید دامنه ایپی هارو بدست بیاره [this repo](https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/providers.json) و اون هارو ریزالو و از ایپی هاش استفاده کنه.
- **additional_domains** (string[]) : اگر دامنه ای دارین که در مخزن وحید موجود نیست میتونی تو این فیلد وارد کنید. [this repo](https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/providers.json) باید به شکل یک ارایه از استرینگ ها ارائه شود.
- **include_custom_ips** (boolean) : مشخص میکنه که اسکریپت باید از لیست فایل ایپی لوکال شما استفاده کنه.
- **custom_ips_file_path** (string) : مسیر فایل لیست ایپی های لوکال.
- **zone_id** (string) : ایدی زون دامنه شما روی کلودفلر که میخواین ساب روی اون ست شه.
- **email** (string) : ایمیل اکانت کلودفلر شما.
- **global_key** (string) : گلوبال کی اکانت کلودفلر شما.
- **max_no_records** (int) : تعداد ماکسیموم ایپی های سالمی که باید روی ساب ست بشود. به ترتیب تاخیر کمتر.
- **sub_domain** (string) : اسم ساب دومین که شما میخواین ایپی ها روش ست بشه رو مشخص کنید.
- **scan_concurrency** (int) : تعداد ترد ها برای اسکن همزمان.
- **upload_speed** (int) : سرعت اپلود مورد نظر برای تست ایپی ها (در حال حاضر تنها تست اپلود ساپورت شده)
- **custom_config** (string) : مسیر کانفیگ کاستوم [CF Scanner](https://github.com/MortezaBashsiz/CFScanner). میتونید از این قسمت متوجه شید چطور کانفیگ کاستوم بسازین [here](https://github.com/MortezaBashsiz/CFScanner/tree/main/bash)

برای ران کردن اسکنر:

```bash
python main.py --config=/path/to/config
```

## اپراتور ها

مقادیر ساپورت شده برای فیلد operator:

- ALL (تمامی اپراتور ها)
- mci (همراه اول)
- mtn (ایرانسل)
- mkh (مخابرات)
- rtl (رایتل)
- hwb (هایوب)
- ast (آسیاتک)
- sht (شاتل)
- prs (پارس آنلاین)
- mbt (مبین نت)
- ask (اندیشه سبز)
- ztl (زیتل)
- psm (پیشگامان)
- shm (شاتل موبایل)
- fnv (فن آوا)
