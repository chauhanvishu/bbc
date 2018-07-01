# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:14:41 2018

@author: aksha
"""

import re
sample_sentence = "A, very very; irregular_sentence"
print = " ".join(re.split('[;,\s_]+', sample_sentence))

