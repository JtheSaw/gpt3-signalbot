import os

import openai
from dotenv import load_dotenv
from signalbot import Command, Context

load_dotenv()


class GPT3Command(Command):
    def describe(self) -> str:
        """Description of the Command."""
        return "Takes your message and gives a reply generated by GPT-3"

    async def handle(self, context: Context):
        """Command Handler.

        Takes the incomming message and replies to it by calling the GPT-3 API

        Args:
            context (Context): Singalbot Message Context of the incomming message
        """
        await context.start_typing()
        openai.organization = os.environ.get("OPENAI_ORGANIZATION")
        openai.api_key = os.environ.get("OPENAI_API_KEY")

        # prompt = f"Marv is a german chatbot that reluctantly answers questions with sarcastic responses:\nYou: {context.message.text}\nMarv: "
        prompt = f"Marv is a german chatbot that answers questions with helpful responses:\nYou: {context.message.text}\nMarv: "

        completion_result = openai.Completion.create(
            model="text-davinci-003",
            # model="gpt-4-32k",
            # model="gpt-3.5-turbo-0301",
            prompt=prompt,
            max_tokens=4000,
            temperature=1.2,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0,
        )
        reply = completion_result.choices[0].text.strip()
        await context.stop_typing()
        await context.send(f"{reply}")
