uses AWS EMR to analyze Wikipedia November 2014 article view counts



uses hadoop streaming with :
mapper.py      map function
reducer.py     reduce function
fed in data from  s3://wikipediatraf/201411-gz/
with results in output

each line is data on a article,
$1 : total views during November 2014
$2 : Article title
$3...$32 [yyymmdd:views]

runner.sh    analyze data

