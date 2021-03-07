import typer

import themagen.tests
import themagen.pdf
import themagen.email
import themagen.plot

app = typer.Typer()

@app.command()
def gentests():
    typer.echo('Generating tests as Markdown files')
    themagen.tests.generate()


@app.command()
def genpdf():
    typer.echo('Generating PDF attachemnts from Markdown tests')
    themagen.pdf.generate()


@app.command()
def sendmails():
    typer.echo('Sending emails with PDF attachments')
    themagen.email.submit()


@app.command()
def plot(logfilename: str):
    typer.echo('Create plot with historical data')
    themagen.plot.create(logfilename)


if __name__ == "__main__":
    typer.echo('ThemaGen v0.9.0')
    app()
