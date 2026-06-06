import typer

app = typer.Typer() # initialize typer


@app.command()
def store_in_db(word: str):
    pass
    


if __name__ == "__main__":
    app()