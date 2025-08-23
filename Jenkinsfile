pipeline {
  agent any
  stage('maven-install') {
  steps {
    withMaven(maven: 'Maven3', traceability: true) {
      sh 'mvn clean install'
}
  }
}


{
