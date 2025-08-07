import asyncio
from team.dsa_team import create_dsa_team
from config.docker_utils import start_docker_container, stop_docker_container # no used here but i'll try
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult



async def main():
    team, local_exec = create_dsa_team() # if we used docker in code_executor_agent and in create dsa team then
    #await start_docker_container(docker)
    #print("Docker Container Started Successfully")

    try:
        task = TextMessage(
        content="Write a simple Python code to add two numbers.",
        source="User"
    )
        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                print(f"{message.source} : {message.content}")

            elif isinstance(message, TaskResult):
                print(f"Stop Reason :  {message.stop_reason}")
    
    except Exception as e:
        print(f"Error: {e}")

    #finally:
        # print("Stopping Docker Container")
        #await stop_docker_container(docker=docker)


    
if __name__ == "__main__":
    asyncio.run(main())