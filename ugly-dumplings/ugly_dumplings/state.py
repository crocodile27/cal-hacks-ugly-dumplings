"""Base state for the app."""

import reflex as rx


class State(rx.State):
    """The app state."""

    image_url = ""
    image_processing = False
    image_made = False

    def get_dalle_result(self, form_data: dict[str, str]):
        prompt_text: str = form_data["prompt_text"]
        self.image_made = False
        self.image_processing = True
        yield
        try:
            response = openai.Image.create(prompt=prompt_text, n=1, size="1024x1024")
            self.image_url = response["data"][0]["url"]
            self.image_processing = False
            self.image_made = True
            yield
        except:
            self.image_processing = False
            yield rx.window_alert("Error with OpenAI Execution.")
