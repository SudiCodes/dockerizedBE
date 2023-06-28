pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/SudiCodes/dockerizedBE.git']]])
            }
        }
        stage('Build') {
            steps {
                // Add build steps here
            }
        }
        stage('Docker') {
            steps {
                sh 'docker stop dockerizedbe-dockerizedbe-1 || true'
                sh 'docker rm dockerizedbe-dockerizedbe-1 || true'
                
                // Remove the previous image (if any)
                sh 'docker rmi dockerizedbe || true'
                
                // Start the new container using Docker Compose
                sh 'docker-compose up -d'
            }
        // Add more stages as needed
    }
}
