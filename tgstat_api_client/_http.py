from datetime import datetime, timedelta
from typing import Literal

from aiohttp import ClientSession

from .exceptions import ChatNotFound, TGStatError


class HTTPClient:
    def __init__(self, base_url: str, token: str):
        self._session = ClientSession(
            base_url=base_url,
        )
        self._token = token


class TGStatClient(HTTPClient):
    @staticmethod
    def __validate_response(response: dict) -> bool | None:
        if response.get('status') == 'ok':
            return True
        if response.get('status') == 'error':
            if response.get('error') in ('chat_not_found', 'channel_not_found'):
                raise ChatNotFound
            raise TGStatError

    async def _request(self, endpoint: str, params: dict) -> dict:
        async with self._session.get(endpoint, params=params) as response:
            result = await response.json()
            self.__validate_response(result)
            return result.get('response')

    async def get_posts(self, chat: str | int, limit: int = 50, offset: int = 0) -> dict:
        params = {
            'token': self._token,
            'channelId': chat,
            'limit': limit,
            'offset': offset,
        }
        return await self._request('/channels/posts', params)

    async def get_stat(self, chat: str | int) -> dict:
        params = {
            'token': self._token,
            'channelId': chat
        }
        return await self._request('/channels/stat', params)

    async def get_subscribers(self,
                              chat: str | int,
                              start_date: datetime = datetime.now() - timedelta(days=7),
                              end_date: datetime = datetime.now(),
                              group: Literal['hour', 'day', 'week', 'month'] = 'day'):
        params = {
            'token': self._token,
            'channelId': chat,
            'group': group,
            'startDate': start_date.timestamp(),
            'endDate': end_date.timestamp()
        }
        return await self._request('/channels/subscribers', params)

    async def get_views(self,
                        chat: str | int,
                        start_date: datetime = datetime.now() - timedelta(days=7),
                        end_date: datetime = datetime.now(),
                        group: Literal['hour', 'day', 'week', 'month'] = 'day'):
        params = {
            'token': self._token,
            'channelId': chat,
            'group': group,
            'startDate': start_date.timestamp(),
            'endDate': end_date.timestamp()
        }
        return await self._request('/channels/views', params)
