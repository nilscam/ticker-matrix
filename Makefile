default: up

up:
	python -m uvicorn main:app --host 0.0.0.0 --led-rows=64 --led-cols=64 --led-gpio-mapping=adafruit-hat --led-slowdown-gpio=3 --led-chain=2