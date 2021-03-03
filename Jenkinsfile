pipeline {
    agent none
    stages {
        stage('DB') {
            agent {
                docker { image 'wnameless/oracle-xe-11g-r2' }
            }
        }
        stage('App') {
            agent { dockerfile true }
        }
    }
}
