pipeline {
    agent any
    environment {
        DOCKERHUB_CRED = credentials('docker-hub-creds')
    }
    stages {
        stage('build') {
            steps {
                echo 'building'
                sh 'docker compose run -t singhakshitraj/blog-application:1.0.0 --build'
                sh "echo $DOCKERHUB_CRED_PSW | docker login -u $DOCKERHUB_CRED_USR --password-stdin"
            }
        }
        stage('deploy'){
            steps {
                echo 'deploying'
                sh 'docker push singhakshitraj/blog-application:1.0.0'
            }
        }
    }
}