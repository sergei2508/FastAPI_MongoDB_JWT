from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import importlib

from database import startDB

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def start_dependencies():
    try:
        await startDB()
    except Exception as e:
        print(f"Error al iniciar las dependencias: {e}")


def include_routers_from_version(version_folder: str):
    api_path = Path(__file__).parent / 'api' / version_folder
    for module in api_path.glob('routes/*.py'):
        module_name = module.stem
        if module_name == '__init__':
            continue
        module_path = f'api.{version_folder}.routes.{module_name}'
        mod = importlib.import_module(module_path)
        if hasattr(mod, 'router'):
            app.include_router(
                mod.router, prefix=f'/api/{version_folder}', tags=[module_name.capitalize()])


include_routers_from_version('v1')
