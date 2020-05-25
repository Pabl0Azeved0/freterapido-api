message:
	@echo "make build: levantar o container; make run: rodar ele"

build:
	docker build -t flask-app:latest .

run:
	docker run -p 8000:8000 flask-app
