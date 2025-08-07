
async def start_docker_container(docker):
    print("Starting Docker Container...")
    await docker.start()


async def stop_docker_container(docker):
    print("Stopping Docker Container...")
    await docker.start()