node {
    stage('Unit Testing') {
        parallel {
            stage('Front-end tests') {
                def node = tool name: 'Node 8x Current', type: 'jenkins.plugins.nodejs.tools.NodeJSInstallation'
                env.PATH = '${node}/bin:${env.PATH}'
                sh './run_travis.sh frontend'
            }
            stage('Back-end tests') {
                sh './run_travis.sh backend'
            }
            stage('Acceptance tests') {
                def node = tool name: 'Node 8x Current', type: 'jenkins.plugins.nodejs.tools.NodeJSInstallation'
                env.PATH = '${node}/bin:${env.PATH}'
                sh './run_travis.sh acceptance'
            }
        }
    }
    stage('Coverage') {
        parallel {
            stage('Front-End Coverage') {
                sleep 1
                echo 'Hello front-end coverage!'
            }
            stage('Back-End Coverage') {
                sleep 1
                echo 'Hello back-end coverage!'
            }
        }
    }
}
