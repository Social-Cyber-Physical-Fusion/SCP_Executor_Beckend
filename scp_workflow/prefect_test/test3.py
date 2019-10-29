# -*- coding: utf-8 -*-
'''
@Time    :   2019/10/07 21:07:28
@Author  :   Tianyi Wu 
@Contact :   wutianyi@hotmail.com
@File    :   test3.py
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
import prefect
from prefect import task, Flow


def create_spark_cluster():
    print('create_spark_cluster')
    return 'cluster'


def submit_job(cluster):
    print('{} submit_job'.format(cluster))
    return 'submitted'


def tear_down(cluster=None):
    print('{} tear_down'.format(cluster))
    # return 'tear down succeed'


@task
def create_cluster():
    cluster = create_spark_cluster()
    return cluster


@task
def run_spark_job(cluster):
    submit_job(cluster)


@task(trigger=prefect.triggers.always_run)
def tear_down_cluster(cluster):
    tear_down(cluster)


with Flow("Spark") as flow:
    # define data dependencies
    cluster = create_cluster()
    submitted = run_spark_job(cluster)
    stop = tear_down_cluster(cluster)

    # wait for the job to finish before tearing down the cluster
    tear_down_cluster.set_upstream(submitted)

    flow.set_reference_tasks([submitted])

if __name__ == "__main__":
    state = flow.run()
    assert state.is_successful()
