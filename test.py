from autogen_agentchat.agents import AssistantAgent, CodeExecutorAgent
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.code_executors.local import LocalCommandLineCodeExecutor
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core import CancellationToken
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()
key = os.getenv("GROQ_API_KEY")

async def main():
    # 1) Configure the LLM client (now with structured_output=True)
    model_client = OpenAIChatCompletionClient(
        base_url="https://api.groq.com/openai/v1",
        model="llama-3.3-70b-versatile",
        api_key=key,
        model_info={
            "family": "llama",
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "structured_output": True,      # ← new required field
        }
    )

    # 2) Instantiate your two agents
    problem_solver_agent = AssistantAgent(
        name="DSA_Problem_Solver_Agent",
        description="An agent that solves DSA problems",
        model_client=model_client,
        system_message="""

you are a problem solver agent that is an expert in solving DSA problems.
You will be working with code executor agent to execute code.
You will be given a task and you should.
At beginning of your response you have to specify your plan to solve the task in 70 words.
Then you should give code in code block (python).
You should write code in a one code block at a time and then pass it to code executor agent to execute it.
Once the code is executed by code executor agent and of the same has been done successfully, you have the results.
you should explain the code execution result in 50 words.

In the end once the code is executed successfully by code executor agent, you have to say "ok" to stop the conversation.
"""
    )

    local_exec = LocalCommandLineCodeExecutor(work_dir="/tmp", timeout=120)
    code_executor_agent = CodeExecutorAgent(
        name="code_executor_agent",
        code_executor=local_exec
    )

    # 3) Build your team using *instances* of both agents
    termination = TextMentionTermination("STOP")
    team = RoundRobinGroupChat(
        participants=[problem_solver_agent, code_executor_agent],
        termination_condition=termination,
        max_turns=10
    )

    # 4) Define the user task
    task = TextMessage(
        content="Write a simple Python code to add two numbers.",
        source="User"
    )

    # 5) Run the agents in a streaming loop and print outputs
    try:
        #await docker.start()
        async for message in team.run_stream(task=task):
            print("=" * 40)
            # message.content or message.text depending on your API
            print(f"{message.source}: {message.content}")
            print("=" * 40)
    except Exception as e:
        print(f"Error: {e}")

    #finally
        # await docker.stop()

if __name__ == "__main__":
    asyncio.run(main())
