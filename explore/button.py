import ipywidgets as w
from IPython.display import display

btn = w.Button(description="Click Me", button_style = "suceess")

out = w.output()
def on_click(b):
    with out:
        out.clear_output()
        print("Button clicked..")

btn.on_click(on_click)
display(btn, out)