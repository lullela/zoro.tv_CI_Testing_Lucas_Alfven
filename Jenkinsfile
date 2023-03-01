pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/lullela/zoro.tv_CI_Testing_Lucas_Alfven'  // Clone your repository
            }
        }

        stage('Test') {
            steps {
                sh 'python -m unittest main'  // Run your test suite
            }
        }

        stage('Notify') {
            steps {
                echo 'Done'
            }
        }
    }
}
