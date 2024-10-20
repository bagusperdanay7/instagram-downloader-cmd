# Command Line Instagram Downloader Menggunakan Instaloader (Python)

Program super sederhana ini dibuat dalam basis command line, bertujuan untuk mengunduh post instagram menggunakan library `Instaloader` menggunakan bahasa pemrograman `Python`.

## Technology stack & Tools

**Program ini membutuhkan:**

| Language & Library | Version |
| ------------------ | ------- |
| Python             | 3.10+   |
| instaloader        | 4+      |
| python-dotenv      | 1.0     |

## Setup

### Setup File Env

Buka file `.env.example`, rename menjadi `.env` lalu ganti `INSTAGRAM_USERNAME` di file `.env` dengan username instagram anda.

### Install Library

Install semua Library yang dibutuhkan:

```bash
pip3 install -r requirements.txt
```

Atau install satu per satu:

Install library `instaloader` menggunakan pip

```bash
pip3 install instaloader
pip3 install --upgrade instaloader
```

Install library `python-dotenv` menggunakan pip

```bash
pip3 python-dotenv
```

### Run Program

Kemudian Jalankan Program

```bash
python main.py
```
