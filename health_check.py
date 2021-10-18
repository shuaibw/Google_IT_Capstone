#!/usr/bin/env python3

import psutil as ps
import emails, socket

def cpu_check():
  return ps.cpu_percent(1)>80

def disc_check():
  return ps.disk_usage('/').percent > 80

def ram_check():
  return ps.virtual_memory().available/(1024*1024) < 500

def localhost_check():
  return socket.gethostbyname('localhost')!="127.0.0.1"

def alert(subject, body):
  msg=emails.generate_email(
		"automation@example.com",
		"student-03-ea993cc02501@example.com",
		subject,
		body,
		None
      )
  emails.send_email(msg)


if __name__ == "__main__":
  body="Please check your system and resolve the issue as soon as possible."
  if cpu_check():
    alert("Error - CPU usage is over 80%", body)
  if disc_check():
    alert("Error - Available disk space is less than 20%", body)
  if ram_check():
    alert("Error - Available memory is less than 500MB", body)
  if localhost_check():
    alert("Error - localhost cannot be resolved to 127.0.0.1", body)



