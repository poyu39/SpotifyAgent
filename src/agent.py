from agents import AsyncOpenAI, Agent, OpenAIChatCompletionsModel, Runner
from agents import set_tracing_disabled
from tools import *


class SpotifyAgent:
    def __init__(self, base_url: str, api_key: str, model: str):
        self.client = AsyncOpenAI(
            base_url=base_url,
            api_key=api_key,
        )
        set_tracing_disabled(True)
        self.model = model
    
    def create_agent(self):
        tools = [pause_music, play_music]
        self.agent = Agent(
            tools=tools,
            model=OpenAIChatCompletionsModel(model=self.model, openai_client=self.client),
            name='SpotifyAgent',
            instructions='You are a Spotify assistant, your job is to operate music, you can play, pause music.',
        )
        return self.agent
    
    async def run_workflow(self, input_text: str):
        response = await Runner.run(
            starting_agent=self.agent,
            input=input_text,
        )
        return response