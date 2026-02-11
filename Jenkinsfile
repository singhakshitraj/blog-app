pipeline {
    agent any

    parameters {
        string(name: 'IMAGE_NAME', defaultValue: 'singhakshitraj/blog-application', description: 'Docker image name')
        string(name: 'IMAGE_TAG', defaultValue: '1.0.0', description: 'Docker image tag')
    }

    environment {
        DOCKERHUB_CRED = credentials('docker-hub-creds')
    }

    stages {

        stage('Build Image') {
            steps {
                sh "docker build -t ${params.IMAGE_NAME}:${params.IMAGE_TAG} ."
            }
        }

        stage('Login to DockerHub') {
            steps {
                sh """
                echo ${DOCKERHUB_CRED_PSW} | docker login \
                -u ${DOCKERHUB_CRED_USR} \
                --password-stdin
                """
            }
        }

        stage('Push Image') {
            steps {
                sh "docker push ${params.IMAGE_NAME}:${params.IMAGE_TAG}"
            }
        }

        stage('Deploy') {
            steps {
                withCredentials([file(credentialsId: 'blog-env-file', variable: 'ENV_FILE')]) {
                    sh """
                    docker compose --env-file $ENV_FILE up -d
                    """
                }
            }
        }
    }
}
