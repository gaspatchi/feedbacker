from aiohttp import web
from middlewares.validate import validateJson
from routes.feedback import createFeedback, selectCount
from routes.metrics import showMetrics
from utils.config import config
from utils.hooks import registerService, shutdowService

app = web.Application(middlewares=[validateJson])

app.router.add_post("/create", createFeedback)
app.router.add_get("/count/{type}", selectCount)

app.router.add_get("/metrics", showMetrics)

app.on_startup.append(registerService)
app.on_shutdown.append(shutdowService)

web.run_app(app,host=config["server"]["address"],port=config["server"]["port"])
