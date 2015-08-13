Taskwarrior Start Actions Hook
------------------------------------------------

This is a hook for TaskWarrior (http://www.taskwarrior.org),
which allows configurable actions to be initiated on 'task ID start'. 

Install
-------

Note: This hook has been written to leverage taskpirate, for greater hook efficiency.
Please see https://github.com/tbabej/taskpirate for instructions. Don't worry, it's straightforward.

```
git clone https://github.com/linuxcaffe/task.start-actions
cp task.start-actions/on-* ~/.task/hooks/
```

This hook leverages tasklib, so you need to install that too:

```
pip install tasklib
```

Use case
--------

