import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
app = FastAPI()
@app.get('/')
def read_stuff():
    return {'message':'hello-word'}
@app.get('/item', response_class=HTMLResponse)
async def read_item(request: Request, id:str):
    return templates.TemplateResponse(("item.html"),{"request": request, "id":id})
if __name__ == '__main__':
    uvicorn.run(app)
