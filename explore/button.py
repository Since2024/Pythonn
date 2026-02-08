import ipywidgets as w
from IPython.display import display

# Create button
btn = w.Button(
    description="Click Me",
    button_style="success"
)

# Create output area
out = w.Output()

# Click handler
def on_click(b):
    with out:
        out.clear_output()
        print("Button clicked!")

# Link button to function
btn.on_click(on_click)

# Display widgets
display(btn, out)
