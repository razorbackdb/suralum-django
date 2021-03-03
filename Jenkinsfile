pipeline {
    agent none
    stages {
        stage('DB') {
            agent {
                docker { image 'wnameless/oracle-xe-11g-r2' }
            }
            steps {
                sh 'echo "Hey!"'
            }
        }
        stage('App') {
            agent { dockerfile true }
            steps {
                sh 'python --version'
            }
        }
    }
}
