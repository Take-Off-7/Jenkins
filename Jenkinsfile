pipeline {
    agent any

    stages {
        stage('maven-install') {
            steps {
                withMaven(maven: 'Maven3', traceability: true) {
                    bat 'mvn clean install'  // Use 'bat' for Windows
                }
            }
        }
    }
}
