# PSV Parser

## __Requirements__
* You must have [Docker](https://www.docker.com/get-started) installed and running

## __To Run__
1. Open your terminal and navigate to the root of this project
1. Build the Docker image with: `docker build -t parser .`
1. Run the app with: `docker run -it --mount type=bind,source="$(pwd)",target=/app parser python main.py --filename {filename}` making sure to supply the filename arg with a file from the __data__ directory

## __To Test__
1. Open your terminal and navigate to the root of this project
1. Build the Docker image with: `docker build -t parser .`
1. Run the test suite `docker run -it --mount type=bind,source="$(pwd)",target=/app --env ENV=test parser pytest`