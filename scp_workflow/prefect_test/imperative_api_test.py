# -*- coding: utf-8 -*-
'''
@Time    :   2019/10/07 19:56:00
@Author  :   Tianyi Wu 
@Contact :   wutianyi@hotmail.com
@File    :   test2.py
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
from prefect import Flow, Parameter, task, Task

@task
def say_hello(person: str):
    print("Hello, {}!".format(person))

class AddTask(Task):

    def __init__(self, default: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = default

    def run(self, x: int, y: int=None) -> int:
        if y is None:
            y = self.default
        return x + y

# initialize the task instance
add = AddTask(default=1)

if __name__ == "__main__":
    flow = Flow("My imperative flow!")

    # define some new tasks
    name = Parameter("name")
    second_add = add.copy()

    # add our tasks to the flow
    flow.add_task(add)
    flow.add_task(second_add)
    flow.add_task(say_hello)

    # create non-data dependencies so that `say_hello` waits for `second_add` to finish.
    say_hello.set_upstream(second_add, flow=flow)

    # create data bindings
    add.bind(x=1, y=2, flow=flow)
    second_add.bind(x=add, y=100, flow=flow)
    say_hello.bind(person=name, flow=flow)

    flow.run(name='my test')