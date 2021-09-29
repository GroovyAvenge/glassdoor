#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 17:42:51 2021

@author: scottswasey
"""

import glassdoorscraper as gs
import pandas as pd

path="/Users/scottswasey/Libraries/chromedriver-2"

df = gs.get_jobs('data scientist', 5, False, path, 5)