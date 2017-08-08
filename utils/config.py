import os
config = {
    "server": {
        "name": "feedbacker",
        "address": "127.0.0.1",
        "port": 8090,
    },
    "consul": {
        "address": "127.0.0.1",
        "port": 8500,
    },
    "tarantool": {
        "address": "",
        "port": "",
		"user": os.environ.get("tarantool_user"),
		"password": os.environ.get("tarantool_password")
    }
}