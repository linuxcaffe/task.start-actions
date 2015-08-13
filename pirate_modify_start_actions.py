#!/usr/bin/python

import sys
import os
from tasklib.task import TaskWarrior

# wiki actions
# if task has taskwiki backlink annotation, use that
# if task has +wiki tag and proj.any: , but no backlink, open $WIKIDIR/[roject/projname.project.wiki
# if task has +wiki tag, but no backlink or project, open $WIKIDIR/index.wiki

def hook_test(task):
        if task.active and not task.original.get('start'):
                    print("This is a working example.")

# tasknote actions
# if task has tasknote, open that
# if task has +note tag, but no tasknote, open new tasknote
