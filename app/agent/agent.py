from langchain_openai import ChatOpenAI
from config.settings import OpenAISettings

# TODO: Implement Agent class that will handle the logic of the application, such as switching between models and modes, and interacting with the LLM. This class will be used in the Streamlit app to manage the state of the application and provide a clean interface for the frontend to interact with the backend.


class Agent:
    def __init__(self):
        self.settings = OpenAISettings()
        self.models_list = self.settings.models
        self.model_name = self.models_list[0]  # Default to the first model
        self.modes_list = self.settings.modes
        self.mode_name = self.modes_list[0]  # Default to the first mode
        self.llm = ChatOpenAI(api_key=self.settings.api_key, model=self.model_name)

    def set_model(self, model_name: str):
        if model_name in self.models_list:
            self.model_name = model_name
            self.llm = ChatOpenAI(api_key=self.settings.api_key, model=self.model_name)
        else:
            raise ValueError(f"Model {model_name} is not available.")

    def set_mode(self, mode_name: str):
        if mode_name in self.modes_list:
            self.mode_name = mode_name
            # Here you can implement specific configurations for each mode
            pass
        else:
            raise ValueError(f"Mode {mode_name} is not available.")
