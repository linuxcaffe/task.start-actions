#!/usr/bin/python

import sys
import os
from tasklib.task import TaskWarrior
def hook_test(task):
        if task.active and not task.original.get('start'):
#              else exit
                    print("This is a working example.")

# any matching actions are performed sequentially, in top-down order

# if envar $TASKDATA exists
#       then TASKDIR=$TASKDATA
#       else TASKDIR=~/.task

# if $TASKDIR/hooks/timelog-hook exists
#    start timelog

# annotate actions
# if +ann tag exists
#    open Annotation: prompt

# tasknote actions
# if envar $TASKNOTES exists
#       then NOTEDIR=$TASKNOTES
#       else NOTEDIR=$TASKDIR/notes
# if task has existing tasknote, open that
# if task has +note tag, but no tasknote, open new tasknote

# wiki actions
# if envar $TASKWIKI exists
#       then WIKIDIR=$TASKWIKI
#       else WIKIDIR=$TASKDIR/wiki
# if task has taskwiki backlink annotation, open that
# if task has +wiki tag and proj.any: , but no backlink, open $WIKIDIR/project/projname.project.wiki
# if task has +wiki tag, but no backlink or project, open $WIKIDIR/index.wiki

# web actions
# if envar $TASKBROWSER exists
#     then WEBAPP=$TASKBROWSER
#     else WEBAPP=elinks
# if task has url annotation, open the first one with $WEBAPP
# if task has +web tag, but no url annotation
#    QUERY=description - firstword (presuming that will be verb [search|research|find] etc)
#    open $WEBAPP $QUERY

# if ../timelog-hook exists
#     stop timelog

