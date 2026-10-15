# 🔐 Keep Your Self Safe

IF YOU DONT HAVE WIDGET INSTALLED PLS DO SO
winget install -e --id Python.Python.3.12       IN THE TERMINAL 

INFORMATION:

Personally, I don't think it will be an everyday utility for most people, since they already have password managers such as Bitwarden or 1password to create and test passwords. But that's not what a project such as this is about.

However, i still don't think people should trust these services as u as the a person aren't involved in most of the autofill/password generation so i added alot of common things in the data field for common password by adding alot of things people would normally keep their password as.

If u feel like u want here to be other changes pls feel free to do so that would make me feel like this project actually mattered

THANK YOU FOR CHECKING MY FIRST EVER PROJECT 

if you have another worries please feel free to contact dawgdawg2008@gmail.com (not my main gmail nor is the gmail i used to create my git hub account)

A lightweight desktop password strength checker and generator built with **pure Python** and **tkinter**. No dependencies, nothing to install.


## Features

- **Live strength meter** with entropy estimate (in bits) and an estimated time-to-crack
- **Requirements checklist**: length, upper/lowercase, numbers, symbols
- **Weakness detection**: common passwords, keyboard/alphabet/number sequences, repeated characters, and dictionary words or names (including leetspeak swaps like `p@ssw0rd`)
- **Breach check** via the [Have I Been Pwned](https://haveibeenpwned.com/Passwords) API using k-anonymity, so only the first 5 characters of the password's SHA-1 hash ever leave your machine
- **Secure password generator** (12–32 characters) using Python's `secrets` module, with one-click copy

## Requirements

- Python 3.8+
- tkinter (included with most Python installs; on Debian/Ubuntu: `sudo apt install python3-tk`)


## How it works

| Step | Description |
|------|-------------|
| Pool size | Estimates the character set used (lower, upper, digits, symbols, unicode) |
| Raw entropy | `length × log2(pool size)` |
| Penalties | Reduced for common passwords, sequences, repeats, low character variety, and embedded words |
| Time to crack | Average guess time assuming 10 billion guesses/second (offline attack) |

## Privacy

Passwords are analysed locally. The optional breach check sends only the first 5 hex characters of the SHA-1 hash to the HIBP range API; your password is never transmitted.

## Disclaimer

Strength ratings are estimates, not guarantees. Use a unique password for every account and a reputable password manager.

