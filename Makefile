app: 
	docker build -t wbg .

web:
	. bin/activate
	python config.py
	docker build -t wbg-web webpage/

run_app:
	docker run -p 5000:5000 wbg &

run_web:
	docker run -p 80:80 wbg-web &

