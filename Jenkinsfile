pipeline {
    agent any

    tools {
        python 'Python3'
    }

    environment {
        VENV = 'venv'
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/your-username/flask-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
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
                echo "Building the Flask application..."
                mkdir -p build
                cp -r . build/
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                echo "Deploying application..."
                mkdir -p /tmp/flask-deploy
                cp -r build/* /tmp/flask-deploy/
                echo "Deployment completed successfully."
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
