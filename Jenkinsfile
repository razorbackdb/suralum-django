pipeline {
    agent none
    stages {
        stage('App') {
            agent { dockerfile true }
            steps {
                sh 'python manage.py runserver 0.0.0.0:8000'
            }
        }
    }
}
