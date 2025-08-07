from autogen_agentchat.agents import CodeExecutorAgent
from autogen_ext.code_executors.local import LocalCommandLineCodeExecutor
from config.constants import WORK_DIR, TIME_OUT
from config.docker_and_local_executor import get_docker_executor, get_local_executor



def get_code_executor_agent():
    """
    Function to get the code executor agent.
    This agent is responsible in executing code.
    It will work with problem solver agent to execute the code.
    """
    # docker = get_docker_executor() # pass this to code executor below 
    local_exec = get_local_executor()
    code_executor_agent = CodeExecutorAgent(
            name="code_executor_agent",
            code_executor=local_exec #   <- pass docker here
        )
    return code_executor_agent,local_exec 