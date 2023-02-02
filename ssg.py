import typer
from ssg.site import Site

app = typer.Typer()

def main(source="content",dest="dist"):
    config = {
        "source": source,
        "dest" : dest
    }
    Site(**config).build()
typer.run(main)