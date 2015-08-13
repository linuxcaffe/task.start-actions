#!/usr/bin/python

import sys
import os
from tasklib.task import TaskWarrior
def hook_test(task):
        if task.active and not task.original.get('start'):
                    print("This is a working example.")

# if envar $TASKDATA exists
#       then $TASKDIR=$TASKDATA
# else $TASKDIR=~/.task

# tasknote actions
# if envar $TASKNOTES exists
#       then $NOTEDIR=$TASKNOTES
#       else $NOTEDIR=$TASKDIR/notes
# if task has existing tasknote, open that
# if task has +note tag, but no tasknote, open new tasknote

# wiki actions
# if envar $TASKWIKI exists
#       then $WIKIDIR=$TASKWIKI
#       else $WIKIDIR=$TASKDIR/wiki
# if task has taskwiki backlink annotation, open that
# if task has +wiki tag and proj.any: , but no backlink, open $WIKIDIR/project/projname.project.wiki
# if task has +wiki tag, but no backlink or project, open $WIKIDIR/index.wiki


