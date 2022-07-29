from fastapi import FastAPI, Request
from jinja2 import Template

app = FastAPI()

@app.get('/page')
async def page(request: Request, idx: str ):
    # x = Request.id
    template = Template(idx)
    return (template.render(variable=idx))
