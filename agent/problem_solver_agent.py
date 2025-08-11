from autogen_agentchat.agents import AssistantAgent
from config.settings import return_model_client

model_client = return_model_client()



def get_problem_solver_agent():
    problem_solver_agent = AssistantAgent(
            name="DSA_Problem_Solver_Agent",
            description="An agent that solves DSA problems",
            model_client=model_client,
            system_message="""
    You are an expert DSA problem‐solver agent.  

    -- On the **first** time you get a task from the user, you MUST:
    1) Outline your plan in 20 words.
    2) Provide the Python code in a single ```python``` code‐block.
    3) Do **not** explain, do **not** say “STOP.”

    -- When you receive a message **from** the CodeExecutorAgent containing the code’s execution output:
    4) Print and Explain that output in 50 words (plain text).
    5) Finally, output exactly `STOP` on its own line.

    """)
    return problem_solver_agent