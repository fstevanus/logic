pipeline {
    agent { docker { image 'python:3.13.0-alpine3.20' } }
    stages {
        stage('run') {
            steps {
                sh 'python logic_1.py'
            }
        }
    }
}
