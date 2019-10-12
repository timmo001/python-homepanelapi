"""Access the Home Panel API."""
import logging
import json
import asyncio
import aiohttp

_LOGGER = logging.getLogger(__name__)


class HomePanelApi:
    """Class for Home Panel API Client."""

    def __init__(self, host: str, port: str, ssl: bool) -> json:
        """Initilalize."""
        self.url = "{}://{}:{}".format("https" if ssl else "http", host, port)
        self.authentication = None

    def authenticate(self, username: str, password: str) -> bool:
        """Authenticate with Home Panel."""
        loop = asyncio.get_event_loop()
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
        if data and data["accessToken"]:
            self.authentication = data
            return True
        if data and data["message"]:
            _LOGGER.error("Error authenticating: %s", data["message"])
        else:
            _LOGGER.error("Error authenticating: Unknown")
        return False

    async def async_authenticate(self, username: str, password: str) -> bool:
        """Authenticate with Home Panel."""
        data = await self.post(
            "/authentication",
            {"strategy": "local", "username": username, "password": password},
        )
        if data and data["accessToken"]:
            self.authentication = data
            return True
        if data and data["message"]:
            _LOGGER.error("Error authenticating: %s", data["message"])
        else:
            _LOGGER.error("Error authenticating: Unknown")
        return False

    def send_command(self, page: str, card: str, command: str) -> json:
        """Send a command to Home Panel."""
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(
            asyncio.wait_for(
                self.post_with_auth(
                    "/controller",
                    {"page": page, "card": card, "command": command},
                ),
                timeout=10.0,
            )
        )

    def get_config(self) -> json:
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(
            asyncio.wait_for(self.get_with_auth("/config"), timeout=10.0)
        )

    async def async_get_config(self) -> json:
        return await self.get_with_auth("/config")

    # pylint: disable=C0330
    async def async_send_command(
        self, page: str, card: str, command: str
    ) -> json:
        """Send a command to Home Panel."""
        return await self.post_with_auth(
            "/controller", {"page": page, "card": card, "command": command}
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
        authorization = "Bearer {}".format(self.authentication["accessToken"])
        async with aiohttp.ClientSession() as session:
            # pylint: disable=C0330
            async with session.post(
                url=url, data=data, headers={"Authorization": authorization}
            ) as response:
                return await response.json()

    async def get_with_auth(self, endpoint: str) -> json:
        """Get from Home Panel with authentication."""
        url = "{}{}".format(self.url, endpoint)
        authorization = "Bearer {}".format(self.authentication["accessToken"])
        async with aiohttp.ClientSession() as session:
            # pylint: disable=C0330
            async with session.get(
                url=url,
                data={"userId": self.authentication["user"]["_id"]},
                headers={"Authorization": authorization},
            ) as response:
                return await response.json()
