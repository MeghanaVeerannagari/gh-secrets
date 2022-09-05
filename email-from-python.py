#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 21:31:11 2021

@author: jm
"""

# %% required libraries
import os
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# %% get email and password from environment variables
EMAIL_SENDER= os.environ.get('EMAIL_SENDER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_RECIPIENT = os.environ.get('EMAIL_RECIPIENT')

def send_email():
    logger.info(f"Email is sent from {EMAIL_SENDER} to {EMAIL_RECIPIENT}")
    return EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECIPIENT
