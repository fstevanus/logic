pipeline {
    agent { docker { image 'python' } }
    stages {
        stage('run') {
            steps {
                sh 'python logic_1.py'
            }
        }
    }
}
