pipeline {
    agent any

    environment {
        VENV = 'venv'
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/USERNAME/flask-jenkins-pipeline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python --version
                python -m venv ${VENV}
                . ${VENV}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                . ${VENV}/bin/activate
                pytest
                '''
            }
        }

        stage('Build Application') {
            steps {
                sh '''
                echo "Building application..."
                mkdir -p build
                cp -r app.py templates requirements.txt build/
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                echo "Simulating deployment..."
                mkdir -p /tmp/flask-deploy
                cp -r build/* /tmp/flask-deploy/
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
