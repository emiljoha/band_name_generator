app: 
	docker build -t emijoh/wikibandgen .

web:
	docker build -t emijoh/wikibandgen-web webpage/

run_app:
	docker run -p 5000:5000 -v config:/app/config emijoh/wikibandgen:latest &

run_web:
	docker run -p 80:80 emijoh/wikibandgen-web:latest &

clean:
	rm *~
	cd config
	rm *~
