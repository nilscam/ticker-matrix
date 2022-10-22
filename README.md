# ticker-matrix

Setup on raspberry :

todo : https://raspberrypi-guide.github.io/programming/run-script-on-boot

Run with :

python -m uvicorn main:app --host 0.0.0.0 --led-rows=64 --led-cols=64 --led-gpio-mapping=adafruit-hat --led-slowdown-gpio=3 --led-chain=2