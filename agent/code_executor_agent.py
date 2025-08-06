from autogen_agentchat.agents import CodeExecutorAgent
from autogen_ext.code_executors.local import LocalCommandLineCodeExecutor
from config.constants import WORK_DIR, TIME_OUT



def get_code_executor_agent():
    local_exec = LocalCommandLineCodeExecutor(work_dir=WORK_DIR, timeout=TIME_OUT)
    code_executor_agent = CodeExecutorAgent(
            name="code_executor_agent",
            code_executor=local_exec
        )
    return code_executor_agent,local_exec 