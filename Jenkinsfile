pipeline {
    agent any

    environment {
        VENV = 'venv'
    }

    stages {

        stage('Install Dependencies') {
            steps {
                bat '''
                python --version
                python -m venv %VENV%
                call %VENV%\\Scripts\\activate
                python -m pip install --upgrade pip
                python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '''
                call %VENV%\\Scripts\\activate
                set PYTHONPATH=.
                pytest
                '''
            }
        }


        stage('Build Application') {
            steps {
                bat '''
                echo Building application...
                if not exist build mkdir build
                xcopy app.py build\\ /Y
                xcopy requirements.txt build\\ /Y
                xcopy templates build\\templates\\ /E /I /Y
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                bat '''
                echo Simulating deployment...
                if not exist C:\\flask-deploy mkdir C:\\flask-deploy
                xcopy build C:\\flask-deploy\\ /E /I /Y
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
