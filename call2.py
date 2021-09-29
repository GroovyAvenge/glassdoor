#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 06:01:05 2021

@author: scottswasey
"""

import glassdoorScraper2 as gs
import pandas as pd

path="/Users/scottswasey/Libraries/chromedriver-2"


df = gs.get_jobs('data scientist',15, False, path, 4)
df.to_csv('Uncleaned_DS_jobs.csv', index=False)

#MainCol > div:nth-child(1) > ul > li.react-job-listing.css-bkasv9.eigr9kq0
