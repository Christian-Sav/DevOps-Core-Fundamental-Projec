pipeline {
    agent any
    stages{
        stage('test') {
            steps {
                dir('flask-app')
                    sh "bash test.sh"
            }
        }
    } 
    post {
        always {
            archiveArtifacts artifacts: "flask-app/htmlcov/*"
        }
    }
}