pipeline {
    agent any

    environment {
        VENV = 'venv'
    }

    stages {

        stage('Clone') {
            steps {
                echo 'Cloning repository...'
                git 'https://github.com/umesh-kodipalli/second-brain.git'
            }
        }

        stage('Setup Python') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                python3 -m venv $VENV
                . $VENV/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Building application...'
                sh '''
                . $VENV/bin/activate
                echo "Build step (Python usually doesn't need compile)"
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '''
                . $VENV/bin/activate
                pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                echo "Deployment step (customize this)"
                '''
            }
        }
    }
}
``
