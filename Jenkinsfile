pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/lullela/zoro.tv_CI_Testing_Lucas_Alfven.git']]])
            }
        }
          stage('Clone') {
            steps {
                git 'https://github.com/lullela/zoro.tv_CI_Testing_Lucas_Alfven.git'  // Clone your repository
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
