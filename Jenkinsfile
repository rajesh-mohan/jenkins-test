pipeline {
    agent any
    stages {
      stage('build') {
        steps {
            withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: '3f9875c2-1c7e-4654-9f2d-d1a971c2a2fe', passwordVariable: 'MY_PASSWORD1', usernameVariable: 'MY_USERNAME1']]) {
                sh 'export MY_PASSWORD=${MY_PASSWORD1} && export MY_USERNAME=${MY_USERNAME1} && python3 test.py' 
          }
        }
      }
    }
}
