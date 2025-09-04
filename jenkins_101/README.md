# Build the Jenkins BlueOcean Docker Image
docker build -t myjenkins-blueocean:2.414.2 .

# Create the network 'jenkins'
docker network create jenkins

# Run the Container - MacOS / Linux
docker run --name jenkins-blueocean \
  --restart unless-stopped \
  --detach \
  --network jenkins \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins-data:/var/jenkins_home \
  myjenkins-blueocean:2.414.2rts/client:ro \