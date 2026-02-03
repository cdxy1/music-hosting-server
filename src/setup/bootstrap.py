import uvicorn

from src.setup.composition_root import app

if __name__ == "__main__":
    uvicorn.run(
        app,
    )
