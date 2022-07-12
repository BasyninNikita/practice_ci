pipeline {
    agent {
        docker {
            image 'funnyzak/java-node-python-go-etc'
            args '-u root:root'
        }
    }

    stages {
        stage('Prepare') {
            steps {
                echo "adin"
                
            }
        }
        
        stage('Get dependencies') {
            
            steps {
                // Get some code from a GitHub repository
                git 'https://github.com/BasyninNikita/practice_ci.git'
                
                sh 'python3 dependencies.py $CI_PROJECT_REPOSITORY_LANGUAGES > deps.txt'
            }
            post {
                always {
                    archiveArtifacts artifacts: 'generatedFile.txt', onlyIfSuccessful: false0
                }
            }
        }
    }
}
