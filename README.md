
# Kuroro Ranch Bot

Register : https://t.me/catgram_play_bot/app?startapp=v4lv1BXuIT

PLEASE READ FIRST

## Installation

1. **Download Python 3.12+**
   - Pastikan kamu sudah memiliki Python versi 3.10 atau yang lebih baru. Kamu bisa mendownloadnya dari [python.org](https://www.python.org/downloads/).

2. **Install Module**
   - Buka command prompt atau terminal, lalu jalankan perintah:
     ```
     pip install requests colorama
     ```
   - Ini akan menginstal dua modul yang diperlukan: `requests` untuk melakukan permintaan HTTP dan `colorama` untuk memberi warna teks di konsol.

3. **Buka Bot CatGram di PC (Telegram Web / Desktop)**
   - Buka Telegram Web atau Telegram Desktop di PC kamu.
   - Cari Bot CatGram (Buka dari bot aslinya, bukan reff)

4. **Ambil query_id**
   - Buka Bot CatGram dan lakukan inspeksi elemen di halaman tersebut.
   - Pergi ke tab Application (biasanya di browser, ada di bagian atas inspector).
   - Pilih `session storage` dan kemudian `play.catgram.io`.
   - Di dalamnya, cari `__telegram_initparam` dan temukan `tgwebappdata`.
   - Ambil nilai `query_id=xxx` (ambil semua nilai ini kecuali `tgwebappnya`).
   - Jika kau mendapat `user=`, itu salah. Harap buka dari bot aslinya (cari catgram, ketik /start, buka bot)

5. **Paste di query.txt**
   - Buat atau buka file `query.txt` dan paste nilai `query_id` yang telah kamu ambil sebelumnya.

6. **Jalankan getoken.py**
   - Buka command prompt dan jalankan :
     ```
     python getoken.py
     ```
   - Jika status Login request was successful!, Maka token sudah tersimpan di token.txt
   - 
8. **Jalankan bot.py**
   - Jika token sudah didapat, jalankan :
     ```
     python bot.py
     ```

DONEE

PLEASE READ FIRST
  
## Features
- Auto Upgrade
- Auto Mining and Feeding
- Auto Checkin Daily
- Multi Account
