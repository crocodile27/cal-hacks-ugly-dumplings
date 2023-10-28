"""Welcome to Reflex!."""

from cal_hacks_ugly_dumplings import styles

# Import all the pages.
from cal_hacks_ugly_dumplings.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()
