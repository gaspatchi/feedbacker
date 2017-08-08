import aiohttp
import jsonschema
import datetime

create_feedback = {
	"type" : "object",
	"required": ["type", "firstname", "lastname", "email", "text"],
	"properties": {
		"type": { "type": "string", "minLength": 4},
		"firstname": { "type": "string", "minLength": 2, "maxLength": 15},
		"lastname": { "type": "string", "minLength": 2, "maxLength": 15},
		"number": { "type": "string", "minLength": 11, "maxLength": 11},
		"email": { "type": "string", "format": "email", "minLength": 2, "maxLength": 50},
		"text": { "type": "string", "minLength": 10}
	}
}

create_claim = {
	"type" : "object",
	"required": ["type", "firstname", "lastname", "number"],
	"properties": {
		"type": { "type": "string", "minLength": 4},
		"firstname": { "type": "string", "minLength": 2, "maxLength": 15},
		"lastname": { "type": "string", "minLength": 2, "maxLength": 15},
		"number": { "type": "string", "minLength": 11, "maxLength": 11},
		"email": { "type": "string", "format": "email", "minLength": 2, "maxLength": 50},
		"text": { "type": "string", "minLength": 10}
	}
}

async def validateJson(app, handler):
	async def middleware_handler(request):
		try:
			if request.path.startswith("/create") and request.method == "POST":
				body = await request.json()
				if body["type"] == "feedback":
					jsonschema.Draft4Validator(create_feedback).validate(body)
					return await handler(request)
				elif body["type"] in ["driving", "hairdresser", "florist"] and request.method == "POST":
					body = await request.json()
					jsonschema.Draft4Validator(create_claim).validate(body)
					return await handler(request)
				else:
					return aiohttp.web.json_response({"message": "Такого типа не существует"}, status=404)
			elif request.path.startswith("/count/") and request.method == "GET":
				if request.match_info.get("type",None)  in ["feedback", "driving", "hairdresser", "florist"]:
					return await handler(request)
				else:
					return aiohttp.web.json_response({"message": "Такого типа не существует"}, status=404)
			else:
				return await handler(request)
		except jsonschema.ValidationError as error:
			return aiohttp.web.json_response({"message": error.message}, status=400)
		except Exception as error:
			print({"type": "Error", "module": "Validate", "section": "validateJson", "message": error.__str__(), "date": datetime.datetime.now().isoformat("T")})
			return aiohttp.web.json_response({"message": "Ошибка при валидации данных"},status=500)

	return middleware_handler