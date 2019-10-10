"""Access the Home Panel API."""
import asyncio
import aiohttp
import json

loop = asyncio.get_event_loop()


class HomePanelApi:
    """Class the Home Panel API."""

    def __init__(self, host: str, port: str, ssl: bool) -> json:
        """Initilalize."""
        self.url = "{}://{}:{}".format("https" if ssl else "http", host, port)

    def authenticate(self, username: str, password: str) -> bool:
        """Authenticate with Home Panel."""
        data = loop.run_until_complete(
            asyncio.wait_for(
                self.post(
                    "/authentication",
                    {
                        "strategy": "local",
                        "username": username,
                        "password": password,
                    },
                ),
                timeout=10.0,
            )
        )
        self.authentication = data["accessToken"]
        return True

    def send_command(self, page: str, card: str, command: str) -> json:
        """Send a command to Home Panel."""
        return loop.run_until_complete(
            asyncio.wait_for(
                self.post_with_auth(
                    "/controller",
                    {"page": page, "card": card, "command": command},
                ),
                timeout=10.0,
            )
        )

    async def post(self, endpoint: str, data: json) -> json:
        """Post to Home Panel."""
        url = "{}{}".format(self.url, endpoint)
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, data=data) as response:
                return await response.json()

    async def post_with_auth(self, endpoint: str, data: json) -> json:
        """Post to Home Panel with authentication."""
        url = "{}{}".format(self.url, endpoint)
        authorization = "Bearer {}".format(self.authentication)
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=url, data=data, headers={"Authorization": authorization}
            ) as response:
                return await response.json()
