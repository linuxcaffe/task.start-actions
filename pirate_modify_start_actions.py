#!/usr/bin/python

import sys
import os
import subprocess
from tasklib.task import TaskWarrior
def hook_test(task):
    if task.active and not task.original.get('start'):
#              else exit
        print("This is a working example.")

# any matching actions are performed sequentially, in top-down order

# if envar $TASKDATA exists
#     then TASKDIR=$TASKDATA
#     else TASKDIR=~/.task

# parse description for verb/ noun/ details components
# example "call Billy Bass about fishing trip"
# VERB=first word of description (call)
# if second word starts upper-case
#    NOUN=upper-cased word(s) (Billy Bass)
#    DETAILS=words after upper-cased one(s) (about fishing trip)
# else NOUN=all words after first word

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
# SEARCH_PREFIX=google:
# if task has url annotation(s), open with $WEBAPP
# if task has +web tag, but no url annotation
#    QUERY=description - firstword (presuming that will be verb [search|research|find] etc)
#    open $WEBAPP $SEARCH_PREFIX $QUERY
# subprocess.Popen(['firefox', 'www.google.com'])


