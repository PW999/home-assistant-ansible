#!/bin/bash
case $1 in
	"debian10")
		export MOLECULE_NAME=debian10
		export MOLECULE_DISTRO=debian
		export MOLECULE_DISTRO_VERSION=10.11
		;;
	"debian11")
		export MOLECULE_NAME=debian11
		export MOLECULE_DISTRO=debian
		export MOLECULE_DISTRO_VERSION=11.2
		;;
	"ubuntu20")
		export MOLECULE_NAME=ubuntu20
		export MOLECULE_DISTRO=ubuntu
		export MOLECULE_DISTRO_VERSION=20.04
		;;
	"ubuntu21")
		export MOLECULE_NAME=ubuntu21
		export MOLECULE_DISTRO=ubuntu
		export MOLECULE_DISTRO_VERSION=21.10
		;;
	"ubuntu22")
		export MOLECULE_NAME=ubuntu22
		export MOLECULE_DISTRO=ubuntu
		export MOLECULE_DISTRO_VERSION=22.04
		;;
	*)
		echo "Invalid distribution name $1, supported names are debian10, ubuntu20, ubuntu21"
		exit 2
		;;
esac

export PY_COLORS=1

# Configuration of the apt-cache caching proxy. See the main README on how to run the proxy
# The IP address is that of the docker0 interface
export APT_CACHE_IP=172.18.0.1
export APT_CACHE_PORT=3142
