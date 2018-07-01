# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re
test_emails = """zuck26@facebook.com page33@google.com jeff42@amazon.com"""
print(re.findall(r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})', test_emails,flags=re.IGNORECASE))