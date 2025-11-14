IMAGE := sii-clip
PROJECT_DIR := $(shell pwd)

# Build image
build:
	docker build -t $(IMAGE) .

# Open shell inside container
shell:
	docker run -it \
		--shm-size=8g \
		-v $(PROJECT_DIR):/opt/project \
		-v $(PROJECT_DIR)/outputs:/opt/project/outputs \
		--rm \
		$(IMAGE) /bin/bash

# Run model_1 (por ejemplo BLIP)
run-model1:
	docker run \
		--shm-size=8g \
		-v $(PROJECT_DIR):/opt/project \
		-v $(PROJECT_DIR)/outputs:/opt/project/outputs \
		--rm \
		$(IMAGE) python /opt/project/main.py --model model_1

# Run model_2 (por ejemplo ViT-GPT2)
run-model2:
	docker run \
		--shm-size=8g \
		-v $(PROJECT_DIR):/opt/project \
		-v $(PROJECT_DIR)/outputs:/opt/project/outputs \
		--rm \
		$(IMAGE) python /opt/project/main.py --model model_2
