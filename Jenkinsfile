pipeline {
    agent any
    stages {
      stage('build') {
        steps {
            withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: '1107ac15-dad3-4149-9028-826a6ed97a3e', passwordVariable: 'MY_PASSWORD1', usernameVariable: 'MY_USERNAME1']]) {
                sh 'export MY_PASSWORD=${MY_PASSWORD1} && export MY_USERNAME=${MY_USERNAME1} && python3 test.py' 
          }
        }
      }
    }
}
