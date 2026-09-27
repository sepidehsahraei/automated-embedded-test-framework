pipeline {
    agent any
stages {
    stage('Install Dependencies') {
        steps {
            bat '"C:\\Users\\Sepideh\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt'
        }
    }

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