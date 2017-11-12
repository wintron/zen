#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os


def handler(*args, **kwargs):
    return "hello world"


if __name__ == "__main__":
    print lambda_handler(*sys.argv)
