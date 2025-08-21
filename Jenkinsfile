pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-northeast-2'
        SSH_HOST = '15.164.226.178'
        SSH_USER = 'ubuntu'
    }

    stages {
        stage("Fetch Secret from AWS") {
            steps {
                script {
                    def secretJson = sh(
                        script: "aws secretsmanager get-secret-value --secret-id login-app-secrets --region ${env.AWS_REGION} --query SecretString --output text",
                        returnStdout: true
                    ).trim()
                    def parsed = readJSON text: secretJson
                    env.SECRET_KEY = parsed.secret_key
                }
            }
        }

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
                    export SECRET_KEY=${env.SECRET_KEY} && \
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
