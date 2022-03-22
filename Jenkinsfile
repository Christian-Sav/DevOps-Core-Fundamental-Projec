pipeline {
    agent any
    stages{
        stage('test') {
            steps {
                sh "bash flask-app/test.sh"
            }
        }
    } 
    psst {
        always {
            archiveArtifacts artifacts: "htmlcov/*"
        }
    }
}