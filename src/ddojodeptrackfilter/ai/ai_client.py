from langchain_openai import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    )

from langchain.output_parsers import PydanticOutputParser
from typing import Type

from pydantic import BaseModel
from ddojodeptrackfilter.settings import settings

class OpenRouterAIClient:

    def __init__(
        self,
        system_prompt: str,
        human_prompt: str,
        response_format: Type[BaseModel],
        model_name: str,
        temperature: float,
        api_base: str,
        api_key: str
    ):

        self.api_base = api_base
        self.api_key = api_key
        self.model_name = model_name
        self.temperature = temperature 

        self.chat = ChatOpenAI(
            model_name= self.model_name,
            temperature=self.temperature,
            openai_api_base=self.api_base,
            openai_api_key=self.api_key
        )

        self.response_format = response_format 
        self.parser = PydanticOutputParser(pydantic_object=self.response_format)
        self.schema_instructions = self.parser.get_format_instructions()

        self.system_message = SystemMessagePromptTemplate.from_template(system_prompt + "\n{schema_instructions}")
        self.human_message = HumanMessagePromptTemplate.from_template(human_prompt + "\n{text}")

        self.prompt = ChatPromptTemplate.from_messages([
            self.system_message,
            self.human_message
        ])

    
    def parse(self,raw_text: str) -> BaseModel:
        formatted = self.prompt.format(
                text=raw_text,
                schema_instructions=self.schema_instructions
            )
        response = self.chat.invoke(formatted)
        return self.parser.parse(response.content)
