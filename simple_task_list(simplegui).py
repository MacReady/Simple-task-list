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
    
