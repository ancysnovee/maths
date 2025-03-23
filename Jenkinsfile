pipeline{
    agent any
    stages{
        stage ("clone repo"){
            steps{
                url:"https://github.com/ancysnovee/maths.git", branch:"main"
            }
        }
        stage ("dependency"){
            steps{
                echo "installing virtual machine"
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    python -m pip --upgrade pip
                    pip install pytest
                    '''
            }
        }
        stage ("testing") {
            steps{
                bat '''
                    call venv\\Scripts\\activate
                    pytest test.py
                    '''

            }
        }
        stage ("deploy") {
            echo "displaying application"
            bat '''
                call venv\\Scripts\\activate
                python adding.py
                python sub.py
                '''
        }
    }

}