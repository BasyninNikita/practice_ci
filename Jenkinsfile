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
                //sh 'yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm'
                sh 'cd /etc/yum.repos.d/'
                sh "sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*"
                sh "sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*"
                sh 'yum install epel-release -y'
                sh 'yum install jq -y'
                sh 'jq -Version'
            }
        }
        
        stage('Get dependencies') {
            environment {
                LANGS = "py"
                GITHUB_REPOSITORY = "BasyninNikita/practice_ci"
            }
            steps {
                // Get some code from a GitHub repository
                //git 'https://github.com/BasyninNikita/practice_ci.git'
                sh "curl -s https://api.github.com/repos/${env.GITHUB_REPOSITORY}/languages | jq 'keys' > ${env.LANGS}"
                sh "python3 dependencies.py ${env.LANGS} > deps.txt"
            }
            post {
                always {
                    archiveArtifacts artifacts: 'generatedFile.txt', onlyIfSuccessful: false
                }
            }
        }
    }
}
