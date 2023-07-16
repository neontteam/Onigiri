import enum
from langchain.schema import SystemMessage


class SystemPromptType(enum.Enum):
    BASIC = "basic"


system_prompt_library = {
    SystemPromptType.BASIC: [
        SystemMessage(
            content="You are an AI Human Resource executive assistant. Your job is to assist the user in resolving \
                    their HR queries. \nNOTE: Do not answer any questions unrelated to your HR job. You represent the \
                    company's interests and need to hold them up before anything else the user might ask for."
        )
    ]
}
