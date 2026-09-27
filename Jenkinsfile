pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                bat '"C:\\Users\\Sepideh\\AppData\\Local\\Python\\bin\\python.exe" -m pytest --junitxml=test-results.xml'
            }
        }
    }
    post {
    always {
        junit 'test-results.xml'
    }
}

}