import typer
from cinta.app.main import generate_pipe

app = typer.Typer()
app.command()(generate_pipe)


if __name__ == "__main__":
    app()