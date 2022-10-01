# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 15:01:25 2022

@author: tungd
"""
import glassdoor_scraper as gs
import pandas as pd

df = gs.fetch_jobs('data scientist', 5)