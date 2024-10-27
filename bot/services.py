import os
import aiohttp

from typing import Union
from dotenv import load_dotenv

load_dotenv()
API_HOST = os.getenv('API_HOST')
API_PORT = os.getenv('API_PORT')


class QuestionService:
    BASE_URL = f'http://{API_HOST}:{API_PORT}/questions/'

    def __init__(self, telegram_id: Union[int, str]):
        self._url = self.BASE_URL + str(telegram_id)

    async def get_question(self) -> str:
        session = aiohttp.ClientSession()

        try:
            response = await session.get(self._url)
            data = await response.json()

            if response.status in (200, 404):
                return data.get('data', None)

            return 'Something went wrong ...'

        except Exception as e:
            return f'error: {e}'

        finally:
            await session.close()
