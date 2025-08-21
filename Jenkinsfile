pipeline {
    agent any
    environment {
        SECRET_KEY = credentials('secret_key')
        SSH_HOST = '15.164.226.178'
        SSH_USER = 'ubuntu'
    }
    stages {
        stage("Clone Repo") {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'ssh_id', keyFileVariable: 'SSH_KEY')]) {
                    sh """
                    ssh -o StrictHostKeyChecking=no -i $SSH_KEY $SSH_USER@$SSH_HOST '
                    git clone https://github.com/krishnan1412/Secure-Login-App.git'
                    """
                }
            }
        }
        stage("Build Docker Image") {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'ssh_id', keyFileVariable: 'SSH_KEY')]) {
                    sh """
                    ssh -o StrictHostKeyChecking=no -i $SSH_KEY $SSH_USER@$SSH_HOST '
                    cd Secure-Login-App && \
                    sudo docker-compose up -d --build'
                    """
                }
            }
        }
    }
    post {
        success {
            echo "Deployment successful!"
        }
        failure {
            echo "Deployment failed!"
        }
    }
}
