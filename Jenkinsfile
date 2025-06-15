pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t stadtinfo-api .'
            }
        }
    }
}
