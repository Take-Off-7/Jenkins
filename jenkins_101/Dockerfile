# Start from Jenkins LTS with JDK 11
# FROM jenkins/jenkins:2.452.2-lts-jdk11 -> old
FROM jenkins/jenkins:2.516.2-lts-jdk17


# Switch to root to install system packages
USER root

# Install required packages (lsb-release, pip, curl, docker-cli)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       lsb-release \
       python3-pip \
       curl \
       gnupg \
    # Add Docker’s official GPG key
    && curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
       https://download.docker.com/linux/debian/gpg \
    # Add Docker repository
    && echo "deb [arch=$(dpkg --print-architecture) \
       signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
       https://download.docker.com/linux/debian \
       $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list \
    # Install Docker CLI
    && apt-get update \
    && apt-get install -y --no-install-recommends docker-ce-cli \
    # Cleanup to keep image small
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy plugin list from local directory into the image
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt

# Install Jenkins plugins listed in plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

# Switch back to Jenkins user (best practice)
USER jenkins
