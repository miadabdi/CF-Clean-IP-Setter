# CF-Clean-IP-Setter

[نسخه فارسی مستند](README-FA.md)

Test CloudFlare public ips and local file of ips and automatically set them to domain on CloudFlare.

It can retrieve and scan ips, and it can set them to a domain Or you can provide the result file and skip the scanning part of it.

** Only usable with Vmess+WS+TLS configs **

## Installation

Clone the repo:

```bash
git clone https://github.com/miadabdi/CF-Clean-IP-Setter.git && cd CF-Clean-IP-Setter
```

Clone CFScanner repo and prepare for execution:

```bash
git clone https://github.com/MortezaBashsiz/CFScanner.git && chmod +x CFScanner/bin/*
```

Also, CFScanner requires some dependencies, docs [here](https://github.com/MortezaBashsiz/CFScanner/tree/main/bash#requirements).

Install dependencies:

```bash
pip install -r ./requirements.txt
```

### Configuration

Before running the program you should provide a config, copy `config.json.example` to some file name like `config.json` and delete the comments.

```bash
cp config.json.example config.json
```

Theses are the values:

- **operator** (string) : The operator to retrieve the ips for. when providing a custom local list of ips, this option has no effect, but when fetching public ips this will effect since public ips come with information of what operator they should be used for.
- **use_provided_result** (boolean) : determines if the program should use a provided result file and skip scanning or scan ips to create result itself. The result file is compatible with the result file of bash version of [CF Scanner](https://github.com/MortezaBashsiz/CFScanner).
- **last_result_path** (string) : path to provided result file.
- **include_list_ips** (boolean) : determines if the program should fetch ips from [this repo](https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/list.json)
- **include_list_domains** (boolean) : determines if the program should fetch domains from [this repo](https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/providers.json) and resolve them to use their ips for scanning.
- **additional_domains** (string[]) : if you have your own domains which is not included in [this repo](https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/providers.json) you can provide them to this list of strings.
- **include_custom_ips** (boolean) : determines if the program should use local list of ips for scanning.
- **custom_ips_file_path** (string) : path to local list of ips.
- **zone_id** (string) : zone id of your domain.
- **email** (string) : email of your CF account.
- **global_key** (string) : global key of your CF account.
- **max_no_records** (int) : max number of clean ips (sorted by delay) to be set on your sub domain.
- **sub_domain** (string) : the sub domain you would like the clean ips to be set on.
- **scan_concurrency** (int) : number of threads, to scan ips concurrently.
- **upload_speed** (int) : desired speed of upload for scanning. (at the moment this script only supports upload testing)
- **custom_config** (string) : path to custom config for [CF Scanner](https://github.com/MortezaBashsiz/CFScanner). You can figure out how to create one [here](https://github.com/MortezaBashsiz/CFScanner/tree/main/bash)

To run the program now run:

```bash
python main.py --config=/path/to/config
```

## Operators

Supported operator values:

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
