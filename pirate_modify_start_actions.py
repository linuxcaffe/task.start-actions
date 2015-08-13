#!/usr/bin/python

import sys
import os
from tasklib.task import TaskWarrior

def hook_test(task):
        if task.active and not task.original.get('start'):
                    print("This is a working example.")

