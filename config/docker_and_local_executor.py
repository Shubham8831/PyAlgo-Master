from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from autogen_ext.code_executors.local import LocalCommandLineCodeExecutor
from config.constants import WORK_DIR, TIME_OUT

def get_docker_executor():
    """
    Function to get Docker comand line executor.
    This will run the code in Docker container.
    """
    docker_executor = DockerCommandLineCodeExecutor(
        work_dir=WORK_DIR,
        timeout=TIME_OUT
    )
    return docker_executor


def get_local_executor():
    """
    Function to get Local command line executor.
    This will run the code in local.
    """
    local_executor = LocalCommandLineCodeExecutor(
        work_dir=WORK_DIR,
        timeout=TIME_OUT
    )
    return local_executor