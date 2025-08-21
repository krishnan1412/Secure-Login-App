pipeline {
    agent any
    environment {
        SECRET_KEY = credentials('secret_key')
        SSH_ID= credentials('ssh_id')
        SSH_HOST = credentials('ssh_host')
        SSH_USER = credentials('ubuntu')
    }
    stages {
        stage ("login and clone the repository in the server") {
            withCredentials([sshUserPrivateKey(credentialsId: 'ssh_id', keyFileVariable: 'SSH_KEY')]) {
                steps {
                    sh """ 
                    ssh -o StrictHostKeyChecking=no -i $SSH_KEY $SSH_USER@$SSH_HOST '
                    git clone "https://github.com/krishnan1412/Secure-Login-App.git" '
                    """
                }
            }
            
        }
        stage ("build the docker image") {
            steps {
                sh """
                ssh -o StrictHostKeyChecking=no -i $SSH_KEY $SSH_USER@$SSH_HOST '
                cd Secure-Login-App && \
                sudo docker-compose up -d --build'
                """
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
}