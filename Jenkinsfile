pipeline {
    agent {
        nodeName 'local-system' // Or use 'label' with the specific node name
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/SudiCodes/dockerizedBE.git']]])
            }
        }
        stage('Copy File') {
            steps {
                sh 'cp /home/v2/workspace/dockerizedBE/mt_backend/mt_backend/be_secrets.py /home/v2/workspace/workspace/test-28-jun-18-57_main/mt_backend/mt_backend'
            }
        }
        stage('Build') {
            steps {
                sh 'docker stop dockerizedbe-dockerizedbe-1 || true'
                sh 'docker rm dockerizedbe-dockerizedbe-1 || true'
                
                // Remove the previous image (if any)
                sh 'docker rmi dockerizedbe || true'
                
                // Start the new container using Docker Compose
                sh 'docker-compose up -d'
            }
        }
    }
}


