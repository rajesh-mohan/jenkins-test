pipeline {
    agent any
    stages {
      stage('build') {
        steps {
            withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: '2d136b2d-1ceb-4312-80dc-be9105501d5b', passwordVariable: 'MY_PASSWORD1', usernameVariable: 'MY_USERNAME1']]) {
                sh 'export MY_PASSWORD=${MY_PASSWORD1} && export MY_USERNAME=${MY_USERNAME1} && python3 test.py' 
          }
        }
      }
    }
}
