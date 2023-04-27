from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import VSplit, Window, HSplit
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.widgets import Frame
from prompt_toolkit import HTML
from prompt_toolkit.layout.dimension import D


class DemoContainer:
    def __init__(self) -> None:
        self.container = Window(
            content=FormattedTextControl(
                text="hello",
                focusable=True,
            ),
            cursorline=True,
        )

    def __pt_container__(self):
        return self.container


frame = Frame(body=DemoContainer(), title=HTML("<bold>TODO</bold>"), width=D())

layout = Layout(HSplit([frame]))

app = Application(layout=layout)
app.run()
