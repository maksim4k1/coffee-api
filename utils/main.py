from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# Token
def get_token_expires():
  return int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000) + (1000 * 60 * 60 * 24 * 3)

def check_token_expires(expires: int):
  return (expires - int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)) > 0

# Data Validation
def check_email(email: str) -> bool:
  if len(email) == 0: return False

  # A-Z a-z 0-9 - _ . @
  def is_ok(string):
    symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_.@'
    for letter in string:
      if letter not in symbols: return False
    return True
  
  dog_count = 0
  dot = False
  i = 0

  for letter in email:
    if letter == "@":
      if dog_count == 1 or email[i+1] == "." or i == 0: return False
      else: dog_count = 1
    if letter == "." and dog_count == 1:
      if i+1 == len(email): return False
      else:
        dot = True
    i += 1
  if dot == False or dog_count == 0: return False

  return is_ok(email)

def check_password(password: str) -> bool:
  if 8 > len(password) or len(password) > 16: return False
  # A-Z a-z 0-9 ! # $ % & * + - . < = > ? @
  symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%&*+-.<=>?@'
  for letter in password:
    if letter not in symbols: return False
  return True

def check_username(username: str) -> bool:
  if len(username) > 50: return False
  symbols = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
  for letter in username:
    if letter not in symbols: return False
  return True

def check_title(title: str) -> bool:
  if len(title) > 100 or len(title) == 0: return False
  return True

def check_description(description: str) -> bool:
  if len(description) > 10000: return False
  return True

# Email
def send_email(email: str, message, message_title) -> bool:
  sender: str = "maksbazh2004@gmail.com"
  sender_password: str = "mrgxsiecocytocpc"

  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()

  try:
    server.login(sender, sender_password)
    msg = MIMEText(message)
    msg["Subject"] = message_title
    server.sendmail(sender, email, msg.as_string())

    return True
  except:
    raise ValueError("Пользователь с таким Email не найден")

# Dates
def get_ms_date():
  return int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)