"""Welcome to Reflex!."""

from ugly_dumplings import styles

# Import all the pages.
from ugly_dumplings.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()
