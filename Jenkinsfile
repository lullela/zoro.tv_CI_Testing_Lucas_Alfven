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
                dir('C:/Users/lulle/.jenkins/workspace'){ 
                    bat 'python -m unittest'
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
