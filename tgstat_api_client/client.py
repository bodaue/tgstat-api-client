from datetime import datetime, timedelta
from typing import Literal

from tgstat_api_client._http import TGStatClient
from tgstat_api_client.models.participants_data import ParticipantsData
from tgstat_api_client.models.post import Post
from tgstat_api_client.models.stat import StatChat, StatChannel
from tgstat_api_client.models.views_data import ViewsData


class TGStat:
    BASE_URL = 'https://api.tgstat.ru'

    def __init__(self, token: str):
        self._client = TGStatClient(self.BASE_URL, token)

    async def get_posts(self,
                        chat: str | int,
                        limit: int = 50) -> list[Post]:
        limit = min(limit, 1000)

        result = list()
        while len(result) < limit:
            response = await self._client.get_posts(chat, offset=len(result))
            items = response['items']
            total_count = response['total_count']

            remaining = min(limit - len(result), len(items))
            result.extend(items[:remaining])

            if len(result) == limit or len(result) == total_count or len(items) < 50:
                break

        return [Post(**post) for post in result]

    async def get_stat(self,
                       chat: str | int) -> StatChat | StatChannel:
        stat = await self._client.get_stat(chat)
        if stat.get('peer_type') == 'chat':
            return StatChat(**stat)
        else:
            return StatChannel(**stat)

    async def get_subscribers(self,
                              chat: str | int,
                              start_date: datetime = datetime.now() - timedelta(days=7),
                              end_date: datetime = datetime.now(),
                              group: Literal['hour', 'day', 'week', 'month'] = 'day') \
            -> list[ParticipantsData]:
        data = await self._client.get_subscribers(chat=chat,
                                                  start_date=start_date,
                                                  end_date=end_date,
                                                  group=group)
        return [ParticipantsData(**item) for item in data]

    async def get_views(self,
                        chat: str | int,
                        start_date: datetime = datetime.now() - timedelta(days=7),
                        end_date: datetime = datetime.now(),
                        group: Literal['hour', 'day', 'week', 'month'] = 'day') \
            -> list[ViewsData]:
        data = await self._client.get_views(chat=chat,
                                            start_date=start_date,
                                            end_date=end_date,
                                            group=group)
        return [ViewsData(**item) for item in data]
