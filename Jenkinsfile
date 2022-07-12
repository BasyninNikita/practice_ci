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
                sh 'yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm'
                sh 'yum install jq -y'
                sh 'jq -Version'
            }
        }
        
        stage('Get dependencies') {
            environment {
                LANGS = "py"
            }
            steps {
                // Get some code from a GitHub repository
                //git 'https://github.com/BasyninNikita/practice_ci.git'
                sh 'curl -s https://api.github.com/repos/${GITHUB_REPOSITORY}/languages | jq "keys" > ${env.LANGS}'
                sh 'python3 dependencies.py ${env.LANGS} > deps.txt'
            }
            post {
                always {
                    archiveArtifacts artifacts: 'generatedFile.txt', onlyIfSuccessful: false0
                }
            }
        }
    }
}
