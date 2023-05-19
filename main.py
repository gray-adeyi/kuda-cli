from typer import Typer

app = Typer()

@app.command()
def hello():
    print("Nice")

@app.command()
def bye():
    print("bye!")

def run():
    app()

if __name__ == "__main__":
    run()
