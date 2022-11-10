IMAGE_NAME=data-science-101

test:  # run notebook tests
	docker build -f Dockerfile.local-test -t $(IMAGE_NAME)-local-test:latest .
	docker run -it $(IMAGE_NAME)-local-test:latest
	docker container rm $(IMAGE_NAME)-local-test:latest

stripout:  # remove all cell output in jupyter notebooks
	./scripts/nbstripout.sh
