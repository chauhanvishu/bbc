# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:08:37 2018

@author: aksha
"""
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
print(re.findall(r"\bB\w+", text, flags=re.IGNORECASE))
