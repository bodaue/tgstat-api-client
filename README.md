# tgstat-api-client

## Description

A python client for working with the TGStat API.

## Installation

```Bash
pip install git+https://github.com/bodaue/tgstat-api-client.git
```

## Usage

```Python
from tgstat_api_client.client import TGStat


async def main():
    # Create an instance of the TgStatClient client
    client = TGStat(token="your_token_here")

    # Get channel statistics
    channel_stat = await client.get_stat(chat="channel_id")

    # Get a list of channel posts
    posts = await client.get_posts(chat="channel_id")

    # Get channel views statistics for the last week
    views = await client.get_views(chat="channel_id")

    # Get channel subscribers statistics for the last week
    subscribers = await client.get_subscribers(chat="channel_id")


if __name__ == '__main__':
    asyncio.run(main())
```