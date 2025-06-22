import ipywidgets as widgets
from IPython.display import display, clear_output

def show_error(error_message):
    clear_output(wait=True)
    if not error_message:
        return

    error_box = widgets.HTML(
        value=f"""
        <div style="
            border: 1px solid #fecaca;
            background-color: #fef2f2;
            color: #b91c1c;
            padding: 16px;
            border-radius: 8px;
        ">
            <strong>Error:</strong> {error_message}
        </div>
        """
    )
    display(error_box)
