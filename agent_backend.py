from autogen_agentchat.agents import AssistantAgent, CodeExecutorAgent # agent that generates and executes code snippets based on user
import asyncio
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.code_executors.local import LocalCommandLineCodeExecutor
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from dotenv import load_dotenv
import os
load_dotenv()

key = os.getenv("GROQ_API_KEY")

#model client
model_client =  OpenAIChatCompletionClient(
        base_url="https://api.groq.com/openai/v1",
        model="llama-3.3-70b-versatile",
        api_key = key,
        model_info={
            "family":'llama',
            "vision" :False,
            "function_calling":True,
            "json_output": True
        }
    )
#agent one
probelm_solver_agent = AssistantAgent(
    name  = "DSA_Problem_Solver_Agent",
    description = "An agent that solves DSA problems",
    model_client=model_client,
    system_message='''
you are a problem solver agent that is an expert in solving DSA problems.
You will be working with code executor agent to execute code.
You will be given a task and you should.
At beginning of your response you have to specify your plan to solve the task in 70 words.
Then you should give code in code block (python).
You should write code in a one code block at a time and then pass it to code executor agent to execute it.
Once the code is executed and of the same has been done successfully, you have the results.
you should explain the code execution result in 50 words.

In the end once the code is executed successfully, you have to say "STOP" to stop the conversation.
    
'''
)

termination_condition = TextMentionTermination("STOP")

team = RoundRobinGroupChat(
    participants=[probelm_solver_agent, CodeExecutorAgent]
)
async def main():
    local_exec = LocalCommandLineCodeExecutor(
        work_dir="/tmp",
        timeout=120
    )

    code_executor_agent = CodeExecutorAgent(
        name="code_executor_agent",
        code_executor=local_exec
    )

    task = TextMessage(
        content=''' here is some code
        ```python
print("hello shubham")
a=5
b=3
print(a+b)
        ```

    ''', source="User"
    )

    # await docker.start()
    try:
        result = await code_executor_agent.on_messages(
            messages=[task],
            cancellation_token=CancellationToken()
        )
        print("result is :", result.chat_message.content)

    except Exception as e:
        print(f"Error: {e}")

    # finally:
        # await docker.stop()


if __name__ == "__main__":
    asyncio.run(main())




