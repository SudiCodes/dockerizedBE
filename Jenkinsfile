pipeline {
    agent {
        label 'local-system' // Or use 'label' with the specific node name
    }
    stages {
        stage('Clone') {
            steps {
                sh 'echo clonning git repo ...'
                sh 'git clone https://github.com/SudiCodes/dockerizedBE.git'
                sh 'echo git repo stored in $(pwd)'
            }
        }
        stage('Copy File') {
            steps {
                sh 'cp /home/v2/workspace/dockerizedBE/mt_backend/mt_backend/be_secrets.py /home/v2/workspace/workspace/dockerizedBE_main/mt_backend/mt_backend'
            }
        }
        stage('Build') {
            steps {
                sh 'docker stop be1-dockerizedbe-1 || true'
                sh 'docker rm be1-dockerizedbe-1 || true'
                
                // Remove the previous image (if any)
                sh 'docker rmi dockerizedbe || true'
                
                // Start the new container using Docker Compose
                sh 'docker-compose up -d'
            }
        }
    }
}


