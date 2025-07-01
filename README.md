# Telegram Account Receiver Bot 🤖

Wannan bot ɗin yana sauƙaƙa karɓar sabbin asusun Telegram daga masu siyarwa ta hanyar OTP login (Telethon). An rubuta ta da Aiogram v3, tana amfani da SQLite, kuma tana goyon bayan harshen Hausa da Turanci.

## ⚙️ Features

- 🔑 **OTP Login**: `/start` ➔ tuna lambar waya ➔ karɓi OTP ➔ aika login via Telethon.  
- ❌ **Cancel**: `/cancel` don dakatar da kowane aiki.  
- 📊 **Balance**: `/account_balance` don duba yawan verified/unverified da balance na $0.30 per verified account.  
- 💸 **Withdraw**: `/withdraw` zaɓi NAIRA/USDT ➔ aika account/wallet address.  
- 🌐 **Language**: `/language` don zaɓar “English” ko “Hausa”.  
- 🛡️ **Admin Panel**: `/admin` (Admin only) don ganin total users, verified, unverified.  

## 🚀 Installation

1. Clone repo ko unzip:  
   ```bash
   git clone <your-repo-url>
   cd <project-folder>

2. Girka dependencies:
   ```bash
   pip install -r requirements.txt


3. Tura .env a root da cikakkun bayanai:

BOT_TOKEN=1234567890:ABCDEF_your_token
API_ID=your_api_id
API_HASH=your_api_hash
ADMIN_ID=6281246656


4. Fara bot:
   ```bash
   python main.py



# 📂 Project Structure

telegram_account_bot/  
├── main.py  
├── .env  
├── requirements.txt  
├── database.py  
├── messages.py  
├── README.md  
└── handlers/  
    ├── __init__.py  
    ├── otp_handler.py  
    ├── cancel_handler.py  
    ├── balance_handler.py  
    ├── withdraw_handler.py  
    ├── language_handler.py  
    └── admin_handler.py

# 📘 Commands

Command	Description

/start	Fara login via OTP
/cancel	Soke aiki
/account_balance	Duba stats & balance
/withdraw	Karɓi account/wallet details
/language	Canza harshen bot
/admin	(Admin only) Duba stats na bot



---

# ❗ DISCLAIMER

> Wannan bot don ilimi da masu siyarwa ne kawai.
Ba a goyon bayan amfani da asusun da ba naka ba ko karya doka.
Developer ba zai ɗauki alhakin duk wani amfani mara kyau ba.
Yin amfani da bot ɗin na nufin ka amince da waɗannan sharudda.
