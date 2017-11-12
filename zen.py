#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os


def handler(*args, **kwargs):
    return "i program my home computer, beam myself into the future"


if __name__ == "__main__":
    print handler(*sys.argv)
