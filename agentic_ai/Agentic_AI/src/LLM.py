from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from typing import List
from pydantic import BaseModel, Field
import os

openai_api_key = os.getenv("OPENAI_API_KEY")

class ExampleStructuredOutputSchema(BaseModel):
    query: str = Field(description="The query to be executed")
    tasks_to_be_executed: List[str] = Field(description="The tasks to be executed")


class LLM:
    def __init__(self, model_name: str = "openai:gpt-4o-mini-2024-07-18", temperature: float = 0.1, system_rules: str = ""):
        self.model_name = model_name
        self.temperature = temperature
        self.system_rules = system_rules
        self.llm = self.__initialize_model()

    def __initialize_model(self):
        return init_chat_model(
            model=self.model_name,
            temperature=self.temperature,
            api_key=openai_api_key
        )


    def prompt(self, prompt: str) -> str:
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", self.system_rules),
                ("user", "{input}"),
            ]
        )
        llm = prompt_template | self.llm
        response = llm.invoke({"input": prompt})
        return response
    
class LLMWithTools(LLM):
    def __init__(self, model_name: str = "openai:gpt-4o-mini-2024-07-18", temperature: float = 0.1, tools: List = [], **kwargs):
        super().__init__(model_name, temperature, **kwargs)
        self._tools = tools
        self.llm = self.llm.bind_tools(tools)

    def get_tools(self) -> List:
        return self._tools
    
class LLMWithStructuredOutput(LLM):
    def __init__(self, model_name: str = "openai:gpt-4o-mini-2024-07-18", temperature: float = 0.1, output_schema: BaseModel = {}, **kwargs):
        super().__init__(model_name, temperature, **kwargs)
        self._output_schema = output_schema
        self.llm = self.llm.with_structured_output(output_schema)

    def get_output_schema(self) -> dict:
        return self._output_schema



