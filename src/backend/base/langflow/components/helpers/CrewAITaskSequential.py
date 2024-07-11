from langflow.base.agents.crewai.tasks import SequentialTask
from langflow.custom import Component
from langflow.io import BoolInput, HandleInput, MessageTextInput, Output


class CrewAITaskSequential(Component):
    display_name: str = "CrewAITask (Sequential)"
    description: str = "Each task must have a description, an expected output and an agent responsible for execution."
    documentation: str = "https://docs.crewai.com/how-to/LLM-Connections/"
    icon = "CrewAI"

    inputs = [
        MessageTextInput(
            name="task_description",
            display_name="Description",
            info="Descriptive text detailing task's purpose and execution.",
        ),
        MessageTextInput(
            name="expected_output",
            display_name="Expected Output",
            info="Clear definition of expected task outcome.",
        ),
        HandleInput(
            name="tools",
            display_name="Tools",
            input_types=["Tool"],
            is_list=True,
            info="List of tools/resources limited for task execution. Uses the Agent tools by default.",
            required=False,
            advanced=True,
        ),
        HandleInput(
            name="agent",
            display_name="Agent",
            input_types=["Agent"],
            info="CrewAI Agent that will perform the task",
            required=True,
        ),
        BoolInput(
            name="async_execution",
            display_name="Async Execution",
            value=True,
            advanced=True,
            info="Boolean flag indicating asynchronous task execution.",
        ),
    ]

    outputs = [
        Output(display_name="Task", name="task_output", method="build_task"),
    ]

    def build_task(self) -> SequentialTask:
        task = SequentialTask(
            description=self.task_description,
            expected_output=self.expected_output,
            tools=self.agent.tools,
            async_execution=False,
            agent=self.agent,
        )
        self.status = task
        return task
