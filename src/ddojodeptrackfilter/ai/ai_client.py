from langchain_openai import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    )

from langchain.output_parsers import PydanticOutputParser
from typing import Type, Dict

from pydantic import BaseModel
from ddojodeptrackfilter.settings import settings

import logging

logger = logging.getLogger(__name__)

# TODO: I don't know if it's the best design for ai client. Maybe there is a better one. Need to think of it.

class OpenRouterAIClient:

    def __init__(
        self,
        system_prompt: str,
        human_prompt: str,
        response_format: Type[BaseModel],
        model_name: str,
        temperature: float,
        headers: Dict[str,str],
        api_base: str,
        api_key: str
    ):

        self.model_name = model_name
        self.temperature = temperature
        self.headers = headers
        self.api_base = api_base
        self.api_key = api_key

        self.chat = ChatOpenAI(
            model_name=self.model_name,
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

# TODO: make better design for these functions, they pretty much repeat each other
    
    def get_packages_deptrack_description(self,file_path: str, component_name: str,  raw_text: str) -> BaseModel:
        formatted = self.prompt.format(
                text=raw_text,
                schema_instructions=self.schema_instructions,
                file_path=file_path,
                component_name=component_name
            )
        try:
            response = self.chat.invoke(formatted)
            return self.parser.parse(response.content)
        except (ValueError) as e:
            logger.error(
                "get_packages_deptrack_description failed for %s: %s",
                component_name, e, exc_info=True
            )
            return None


    def get_functions_deptrack_description(self, raw_text: str) -> BaseModel:
        formatted = self.prompt.format(
                text=raw_text,
                schema_instructions=self.schema_instructions
            )
        try:
            response = self.chat.invoke(formatted)
            return self.parser.parse(response.content)
        except (OpenAIError, ValueError) as e:
            logger.error(
                "get_functions_deptrack_description failed for %s: %s",
                component_name, e, exc_info=True
            )
            return None
