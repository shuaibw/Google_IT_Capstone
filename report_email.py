#!/usr/bin/env python3

import os, reports, emails
from datetime import date

os.chdir('./supplier-data/descriptions')
title = "Processed Update on " + str(date.today())

kernel = []

for f in os.listdir():
    if not f.endswith('.txt'):
        continue
    with open(f, 'r') as op:
        lines = op.readlines()[:2]
        to_add = "name: {}<br/>weight: {}<br/>".format(*lines)
        kernel.append(to_add)

if __name__ == "__main__":
    reports.generate_report("/tmp/processed.pdf", title, "<br/>".join(kernel))
    msg = emails.generate_email(
		"automation@example.com",
		"student-03-ea993cc02501@example.com",
		"Upload Completed - Online Fruit Store",
		"All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
		"/tmp/processed.pdf"
    )
    emails.send_email(msg)

