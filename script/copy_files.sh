#! /bin/sh.

HOST="CHANGE THIS"
USER="CHANGE THIS"
DESTPATH="CHANGE THIS"



helpFunction()
{
   echo "Usage: $0 --source[-s] folder/source/route"
   exit 1 # Exit script after printing help
}

_setArgs(){
  while [ "${1:-}" != "" ]; do
    case "$1" in
      "-s" | "--source")
        shift
        routeParam=$1
        ;;
      "-h" | "--help")
        helpFunction
        ;;
    esac
    shift
  done
}

_setArgs $*
scp -r $routeParam $USER@$HOST:$DESTPATH