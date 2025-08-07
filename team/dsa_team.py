from autogen_agentchat.teams import RoundRobinGroupChat
from agent.code_executor_agent import get_code_executor_agent
from agent.problem_solver_agent import get_problem_solver_agent
from autogen_agentchat.conditions import TextMentionTermination
from config.constants import TEXT_MENTION, MAX_TURNS

def create_dsa_team():
    code_executor_agent, local_exec = get_code_executor_agent()
    problem_solver_agent = get_problem_solver_agent()

    termination = TextMentionTermination(TEXT_MENTION)

    team = RoundRobinGroupChat(
            participants=[problem_solver_agent, code_executor_agent],
            termination_condition=termination,
            max_turns=MAX_TURNS
        )
    
    return team, local_exec