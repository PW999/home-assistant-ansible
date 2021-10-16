#!/bin/bash
export PY_COLORS=1
SCOPE=$1
export APT_CACHE_IP=172.17.0.1
export APT_CACHE_PORT=3142
function run_test_for_distro () {
	export MOLECULE_NAME=$1
	export MOLECULE_DISTRO=$2
	export MOLECULE_DISTRO_VERSION=$3

	echo "***********************************************"
	echo "Starting with $MOLECULE_NAME: $MOLECULE_DISTRO:$MOLECULE_DISTRO_VERSION"

	for role in $(ls);
	do
		if [ -f $role ];
		then
			echo "Ignore file $role"
			continue
		fi

		if [ $role == 'resources' ];
		then
			echo "Ignore resources folder"
			continue
		fi
		
		if [ "$SCOPE" != '' ];
		then
			if [ $role != $SCOPE ];
			then
				continue
			fi
		fi

		echo "*** STARTING TEST FOR $role ***"
		mkdir -p /tmp/$MOLECULE_NAME

		cd $role
		file_name="Z_$role-$MOLECULE_NAME"
		echo "Logs are written to $file_name.out"

		MOLECULE_REPORT="../$file_name.html" molecule test > "../$file_name.out" 2>&1
		if [ $? -ne 0 ]; then
			echo "Molecule failed for $role"
			cat ../$file_name.out
			cd ..
			exit 1
		fi
		cd ..
	done
}

run_test_for_distro debian10 debian 10.10
# run_test_for_distro ubuntu20 ubuntu 20.04
run_test_for_distro ubuntu21 ubuntu 21.04
