pipeline {
    agent any
    stages {
        stage('Check out repo'){
            steps {
                checkout scmGit(branches: [[name: '**']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/lullela/zoro.tv_CI_Testing_Lucas_Alfven.git']])
                }
            }
        stage('Test') {
            steps {
                dir('C:/Users/lulle/gitprojekt/zoro.tv_CI_Testing/test_zoro'){ 
                    bat 'python -m unittest main.StartPage'
                }
            }
        }
        stage('Clean Workspace'){
            steps {
                cleanWs()
            }
        }
    }
}
