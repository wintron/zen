#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os


def lambda_handler(event, context):
    total = 0
    
    if "numbers" in event:
        for num in event["numbers"]:
            total += float(num)

    return total


if __name__ == "__main__":
    print lambda_handler(*sys.argv)
