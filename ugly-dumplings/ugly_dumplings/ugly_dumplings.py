"""Welcome to Reflex!."""

from ugly_dumplings import styles
from ugly_dumplings import State

# # Import all the pages.
# from ugly_dumplings.pages import *

import openai
import reflex as rx



def index():
    return rx.center(
        rx.vstack(
            rx.heading("DALL-E", font_size="1.5em"),
            rx.form(
                rx.input(id="prompt_text", placeholder="Enter a prompt.."),
                rx.button(
                    "Generate Image",
                    type_="submit",
                    width="100%",
                ),
                on_submit=State.get_dalle_result,
            ),
            rx.divider(),
            rx.cond(
                State.image_processing,
                rx.circular_progress(is_indeterminate=True),
                rx.cond(
                    State.image_made,
                    rx.image(
                        src=State.image_url,
                        height="25em",
                        width="25em",
                    ),
                ),
            ),
            bg="white",
            padding="2em",
            shadow="lg",
            border_radius="lg",
        ),
        width="100%",
        height="100vh",
        background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    )

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.add_page(index, title="Reflex:DALL-E")
app.compile()
