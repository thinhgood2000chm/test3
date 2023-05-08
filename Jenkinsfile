pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/thinhgood2000chm/test3.git'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}