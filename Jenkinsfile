pipeline {
    agent { docker { image 'jenkins/jenkins:lts' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                echo 'Test Stage'
            }
        }
    }
}
