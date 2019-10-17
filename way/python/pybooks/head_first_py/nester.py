# nested function
def nested(arr):
	for item in arr:
		if isinstance(item, list):
			nested(item)
		else:
			print(item)
