.PHONY : build

create-env :
		-virtualenv powerscheduler

activate-env :
		. powerscheduler/bin/activate; pip install -r requirements.txt;

workspace : create-env activate-env 

clean-workspace :
		-rm -rf powerscheduler;

clean : 
		-find . -name '*.py[co]' -exec rm {} \;


deploy : 
	. powerscheduler/bin/activate; \
	python ./environments/docker_builder.py

docker-build :
	-docker build . -t power-scheduler

docker-run :
	-docker run --name power-scheduler -d -t power-scheduler

docker-stop :
	-docker stop power-scheduler

docker-remove :
	-docker container rm power-scheduler

docker-copy-exe :
	-docker cp power-scheduler:/opt/power-scheduler/ /Users/m873260/power-scheduler
	
docker-copy :
	-docker cp power-scheduler:/opt/power-scheduler/powershell-scheduler.pex ./

get-pex : docker-build docker-run docker-copy docker-stop docker-remove

get-exe : docker-build docker-run docker-copy-exe docker-stop docker-remove