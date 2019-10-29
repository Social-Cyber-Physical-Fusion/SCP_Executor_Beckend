# -*- coding: utf-8 -*-
'''
@Time    :   2019/09/29 14:33:31
@Author  :   Tianyi Wu 
@Contact :   wutianyi@hotmail.com
@File    :   test.py
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
from prefect import Flow, Task, Parameter, task


class AddTask(Task):

    def __init__(self, default: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = default

    def run(self, x: int, y: int = None):
        if y is None:
            y = self.default
        return x + y


# initialize the task instance
add = AddTask(default=1)


@task
def say_hello(person: str):
    print('Hello, {}!'.format(person))


with Flow('Say hi!') as flow:
    name = Parameter('name')
    say_hello(name)


if __name__ == '__main__':
    state = flow.run(name='Marvin')

    print(state.is_successful())

    # state = flow.run()

    # assert state.is_successful()

    # first_task_state = state.result[first_result]
    # assert first_task_state.is_successful()
    # assert first_task_state.result == 2

    # second_task_state = state.result[second_result]
    # assert second_task_state.is_successful()
    # assert second_task_state.result == 103
