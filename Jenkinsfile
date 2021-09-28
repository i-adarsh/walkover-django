pipeline{
    agent none
    stages{
        stage('Stage'){
            agent any
            steps{
                echo "Creating Backup ..."
                echo "Build number is ${currentBuild.number}"
                echo "Previous Build number is ${currentBuild.previousBuild.number}"
                sh "sudo zip -r production${currentBuild.number}.zip /root/production "
                sh "sudo mv production${currentBuild.number}.zip /root/backup"
                sh "sudo rm -f /root/backup/production${currentBuild.previousBuild.number}.zip"
            }       
        }
        stage('Build'){
            agent any
            steps{
                    sh "sudo rm -rf /root/production/accounts"
                    sh "sudo rm -rf /root/production/mcqquiz"
                    sh "sudo rm -rf /root/production/questions"
                    sh "sudo rm -rf /root/production/quiz_app"
                    sh "sudo mv Jenkinsfile /root/production/"
                    sh "sudo mv README.md /root/production/"
                    sh "sudo mv requirements.txt /root/production/"
                    sh "sudo mv LICENSE /root/production/"
                    sh "sudo mv manage.py /root/production/"
            }
        }
        
        stage('Deploy'){
            agent any
            steps{
                sh "sudo systemctl restart gunicorn"
                sh "sudo systemctl restart nginx"
        }
    }
}
}