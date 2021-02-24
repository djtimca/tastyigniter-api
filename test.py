import asyncio
from tastyigniter import TastyIgniter

async def main():
    """Testing function."""
    
    username = input("Username:")
    password = input("Password:")
    domain = input("Domain:")

    api = TastyIgniter(username, password, domain)

    response = await api.get_locations()
    save_file("locations",str(response))

    response = await api.get_enabled_locations()
    save_file("enabled_locations", str(response))

    response = await api.get_orders()
    save_file("orders",str(response))

    response = await api.get_received_orders()
    save_file("received_orders",str(response))

    await api.session.close()

def save_file(fileroot:str,data:str):
    """Save test output to file."""
    f = open(f"test_files/{fileroot}.json", "w")
    f.write(data)
    f.close()

asyncio.run(main())