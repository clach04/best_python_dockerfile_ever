# The best Python Dockerfile ever

Invoking [Cunningham's Law](https://meta.wikimedia.org/wiki/Cunningham%27s_Law), this is the best Dockerfile for a hello world Python web app, in other words https://xkcd.com/386/ ;-)


## Build

    docker build -t best_python_docker .

## Running

Docker Compose:

    echo Open http://localhost:1234/
    docker compose up
    #docker-compose up

Plain docker run:

    echo Open http://localhost:1234/
    #docker run -p 8000:8000 --name best_python_docker --hostname bpd --restart=unless-stopped best_python_docker
    docker run -p 1234:8000 --name best_python_docker --hostname bpd --restart=unless-stopped best_python_docker

## Notes

Useful commands:

    # Show size
    docker images best_python_docker

    # remove container (not image)
    docker rm best_python_docker

    # remove image
    docker image rm best_python_docker

    # show layer sizes
    docker history best_python_docker

    # Connect to running container with an iteractive shell
    docker exec -it best_python_docker /bin/sh

## TODO

  * docker scout quickview
  * https://github.com/clach04/best_python_dockerfile_ever/issues/1
  * Python script update
      * dump current time/date
      * alternative WSGI server
      * external packages to show best practices
  * TODO items in Dockfile
  * Non-root user
  * read only image
  * secrets
  * PORT control
  * .env and env file https://stackoverflow.com/questions/52664673/how-to-get-port-of-docker-compose-from-env-file
  * https://docs.docker.com/compose/compose-file/compose-file-v2/#healthcheck
  * timezone (mount host and TZ env var)
  * DEBUG options
