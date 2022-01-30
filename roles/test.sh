#!/bin/bash
export PY_COLORS=1
# First parameter can be used to change the source test container
DISTRO=$1
# Second parameter can be used to test only a single role
SCOPE=$2

source ./setenv.sh "$DISTRO"

echo "***********************************************"
echo "Starting with $MOLECULE_NAME: $MOLECULE_DISTRO:$MOLECULE_DISTRO_VERSION"

for role in $(ls);
do
	if [ -f "$role" ];
	then
		continue
	fi

	if [ "$role" == 'resources' ];
	then
		continue
	fi

	if [ "$SCOPE" != '' ];
	then
		if [ "$role" != "$SCOPE" ];
		then
			continue
		fi
	fi

	echo "*** STARTING TEST FOR $role ***"
	mkdir -p "/tmp/$MOLECULE_NAME"

	cd "$role" || exit
	file_name="Z_$role-$MOLECULE_NAME"
	echo "Logs are written to $file_name.out"

	MOLECULE_REPORT="../$file_name.html" molecule test > "../$file_name.out" 2>&1
	if [ $? -ne 0 ]; then
		echo "Molecule failed for $role"
		cat "../$file_name.out"
	fi
	cd ..
done
