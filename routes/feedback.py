import aiohttp
import datetime
from utils.metrics import created_feedbacks, count_feedbacks

async def createFeedback(request):
	try:
		body = await request.json()
		response = request.app["tarantool"].call("postForm", body.get("type"), body.get("firstname", None), body.get("lastname", None), body.get("number", None), body.get("email", None), body.get("text", None))
		created_feedbacks.labels(body.get("type")).inc()
		return aiohttp.web.json_response({"id": response[0][0]}, status=200)		
	except Exception as error:
		print({"type": "Error", "module": "Feedback", "section": "createFeedback",
			   "message": error.__str__(), "date": datetime.datetime.now().isoformat("T")})
		return aiohttp.web.json_response({"message": "Невозможно зарегистрировать обращение"}, status=500)


async def selectCount(request):
	try:
		response = request.app["tarantool"].call("postFormCount", request.match_info.get("type"))
		count_feedbacks.inc()
		return aiohttp.web.json_response({"count": response[0][0]}, status=200)
	except Exception as error:
		print({"type": "Error", "module": "Feedback", "section": "selectCount",
			   "message": error.__str__(), "date": datetime.datetime.now().isoformat("T")})
		return aiohttp.web.json_response({"message": "Невозможно получить количество обращений"}, status=500)
