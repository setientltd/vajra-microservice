#!/usr/bin/env groovy

dockerfile {
    dockerRepos = ['setientltd/vajra-microservice']
    mvnPhase = 'package'  // vajra microservice integration-test needs host-based networking, won't work in CI as-is
    mvnSkipDeploy = true
    upstreamProjects = 'confluentinc/rest-utils'
}
