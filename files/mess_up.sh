#!/usr/bin/env bash

if [[ $1 == 1 ]]; then
	kubectl set image deployment workshop hello-workshop=hello-workshop > /dev/null 2>&1
elif [[ $1 == 2 ]]; then
	kubectl set image deployment workshop hello-workshop=hello-workshop:v3 > /dev/null 2>&1
else
	echo 'script only takes arguments "1" or "2"'
fi
