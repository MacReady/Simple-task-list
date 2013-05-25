# Simple task list
# Currently uses simplegui module which is only available when using
# http://www.codeskulptor.org

import simplegui

tasks = []

# Handler for button
def clear():
    global tasks
    tasks = []

# Handler for new task
def new(task):
    tasks.append(task)

# Handler for remove number
def remove_num(tasknum):
    n = int(tasknum)
    if n > 0 and n <= len(tasks):
        tasks.pop(n-1)
    
    
