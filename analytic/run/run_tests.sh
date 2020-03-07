#! /bin/bash

export GEOTOP_PATH=/home/ecor/local/docker/geotop
##export SIMS_PATH=/home/ecor/activity/2020/geotop_article/git/GEOtopExamples/tests/ColdelaPorte/sims 
export SIMS_PATH=/home/ecor/activity/2020/geotop_article/git/GEOtopExamples/tests/Borden05m
echo ls ${SIMS_PATH}


for SIM_PATH in $( ls ${SIMS_PATH}); do
 ##   echo $SIM_PATH
    SIM_PATH=${SIMS_PATH}/${SIM_PATH}
    echo $SIM_PATH
    ${GEOTOP_PATH}/geotop-3.sh ${SIM_PATH}

    cp -R ${SIM_PATH}/output-tabs ${SIM_PATH}/output-tabs_v3
    cp -R ${SIM_PATH}/output-maps ${SIM_PATH}/output-maps_v3
    cp -R ${SIM_PATH}/geotop.log ${SIM_PATH}/geotop_v3.log

    ${GEOTOP_PATH}/geotop-2.sh ${SIM_PATH}
    cp -R ${SIM_PATH}/output-tabs ${SIM_PATH}/output-tabs_v2
    cp -R ${SIM_PATH}/output-maps ${SIM_PATH}/output-maps_v2
    cp -R ${SIM_PATH}/geotop.log ${SIM_PATH}/geotop_v2.log

done

##### ./geotop-3-test-vs-2.sh '/home/ecor/activity/2020/geotop_article/nongit/GEOtopExamples/tests/ColdelaPorte/sims/sim_1' 
## https://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-7.html