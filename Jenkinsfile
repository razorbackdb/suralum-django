pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker-compose build --no-cache'
            }
        }
        stage('Run') {
            steps {
                sh 'docker-compose up -d --force-recreate'
            }
        }
        stage { 'Test' } {
            steps {
                sh './python manage.py jenkins --enable-coverage'
            }
        }
    }
}
