pipeline {
    agent { docker { image 'python:3.13.0-alpine3.20' } }
    stages {
        stage('py-version') {
            steps {
                sh 'python --version'
            }
        }
        stage('run') {
            steps {
                sh 'python logic_1.py'
            }
        }
    }
}
