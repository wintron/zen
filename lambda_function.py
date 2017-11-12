#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import requests


def lambda_handler(*args, **kwargs):
    response = requests.get("https://api.github.com/zen")
    return response.text


if __name__ == "__main__":
    print lambda_handler(*sys.argv)
